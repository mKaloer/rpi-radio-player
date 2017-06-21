import logging

from flask import Flask, jsonify, request, abort, make_response
import flask_sqlalchemy
import flask_restless
from flask_socketio import SocketIO
from flask_cors import CORS
from sqlalchemy import func
from psycogreen.gevent import patch_psycopg
from gevent import monkey
import gevent

import config
import radio_rpc

# Monkey patch (for gevent)
patch_psycopg()
if gevent.version_info[0] == 0:
    monkey.patch_all(thread=False)
else:
    monkey.patch_all(thread=False, subprocess=True)


app = Flask(__name__)
app.config['DEBUG'] = config.DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

socketio = SocketIO(app)
db = flask_sqlalchemy.SQLAlchemy(app)
db.engine.pool._use_threadlocal = False
CORS(app)


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True, nullable=False)
    url = db.Column(db.Unicode, unique=True, nullable=False)
    is_favorite = db.Column(db.Boolean, nullable=False, default=False)


class Log(db.Model):
    """
    Log item for persistent logging of mayor actions.
    """
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    action = db.Column(db.Unicode, nullable=False)
    url = db.Column(db.Unicode, nullable=True)


@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)


@app.route("/play", methods=['POST'])
def play():
    url = request.args.get('url')
    station_id = request.args.get('station_id')
    if url:
        app.logger.debug("Play url: %s", url)
    elif station_id:
        app.logger.debug("Play station: %s", station_id)
        station = Station.query.get(station_id)
        if not station:
            _abort_json(404, message='Station with id {} does not exist'.format(station_id))
        url = station.url
    try:
        status = radio.play(url)
        return _format_status(status)
    except ValueError as e:
        _abort_json(400, message=str(e))


@app.route("/stop", methods=['POST'])
def stop():
    status = radio.stop()
    return _format_status(status)


@app.route("/status")
def radio_status():
    status = radio.get_status()
    return _format_status(status)


def on_status_updated(status):
    app.logger.info("Received status update")
    socketio.emit('status', _format_status(status), json=True, broadcast=True)


def _format_status(status):
    return jsonify({
        'url': status['url'],
        'state': status['state'].name,
        'title': status['title'],
        'name': status['name'],
        'volume': status['volume'],
        'bitrate': status['bitrate'],
    })

def _abort_json(err_code, message):
    abort(make_response(jsonify(
        {
            'msg': message,
            'error_code': err_code
        }), err_code))


radio = radio_rpc.RadioRPC(config.RADIO_GRPC_HOST)
radio.subscribe_to_updates(on_status_updated)

db.create_all()

manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Station, methods=['GET', 'POST', 'PUT', 'DELETE'], url_prefix=config.URL_PREFIX)
manager.create_api(Log, methods=['GET'], url_prefix=config.URL_PREFIX)
