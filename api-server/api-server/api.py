import logging
import json

from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource, Api, marshal
from flask_socketio import SocketIO
from flask_cors import CORS
from sqlalchemy import func, event
from psycogreen.gevent import patch_psycopg
from gevent import monkey
import gevent

import config
import radio_rpc
from models import Station
import resources
import db

# Monkey patch (for gevent)
patch_psycopg()
if gevent.version_info[0] == 0:
    monkey.patch_all(thread=False)
else:
    monkey.patch_all(thread=False, subprocess=True)


app = Flask(__name__)
app.config['DEBUG'] = config.DEBUG
#app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_PATH
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

socketio = SocketIO(app, ping_timeout=60)
CORS(app)


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
        station = db.session.query(Station).filter(Station.id == station_id).first()
        if not station:
            _abort_json(404, message='Station with id {} does not exist'.format(station_id))
        url = station.url
    try:
        status = radio.play(url)
        return jsonify(_format_status(status))
    except ValueError as e:
        _abort_json(400, message=str(e))


@app.route("/stop", methods=['POST'])
def stop():
    status = radio.stop()
    return jsonify(_format_status(status))


def on_status_updated(status):
    with app.app_context():
        try:
            app.logger.debug("Received status update")
            socketio.emit('status', _format_status(status), json=True, broadcast=True)
        except:
            app.logger.warning("Error handling new status", exc_info=True)


@event.listens_for(Station, 'before_update')
def on_favorite_change(mapper, connection, target):
    try:
        app.logger.info("Sending station change event")
        fav_json = marshal(target, resources.station_fields)
        socketio.emit('station', fav_json, json=True, broadcast=True)
    except:
        app.logger.warning("Error handling station change", exc_info=True)


def _format_status(status):
    return marshal(status, resources.status_fields)

def _abort_json(err_code, message):
    abort(make_response(jsonify(
        {
            'msg': message,
            'error_code': err_code
        }), err_code))


radio = radio_rpc.RadioRPC(config.RADIO_GRPC_HOST)
radio.subscribe_to_updates(on_status_updated)

api = Api(app)
api.add_resource(resources.StationListResource, '/stations')
api.add_resource(resources.StationResource, '/stations/<string:id>')
api.add_resource(resources.StatusResource, '/status', resource_class_args=[radio])


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
