from flask import Flask, jsonify, request, abort, make_response
import flask_sqlalchemy
import flask_restless
from flask_cors import CORS
from sqlalchemy import func

import config
import radio_rpc

app = Flask(__name__)
app.config['DEBUG'] = config.DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_PATH
db = flask_sqlalchemy.SQLAlchemy(app)
CORS(app)

radio = radio_rpc.RadioRPC(config.RADIO_GRPC_HOST)

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

db.create_all()

manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Station, methods=['GET', 'POST', 'PUT', 'DELETE'], url_prefix=config.URL_PREFIX)
manager.create_api(Log, methods=['GET'], url_prefix=config.URL_PREFIX)

@app.route("/play", methods=['POST'])
def play():
    url = request.args.get('url')
    station_id = request.args.get('station_id')
    if url:
        app.logger.debug("Play url: %s", url)
    elif station_id:
        app.logger.debug("Play station: %s", station_id)
        url = Station.query.get(station_id).url
        if not url:
            _abort_json(404, message='Station with id {} does not exist'.format(station_id))
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


def _format_status(status):
    return jsonify({
        'url': status['url'],
        'state': status['state'].name
    })

def _abort_json(err_code, message):
    abort(make_response(jsonify(
        {
            'msg': message,
            'error_code': err_code
        }), err_code))
