from flask_restful import Resource, fields, marshal_with, abort, reqparse

from models import Station
import db

station_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'url': fields.String,
    'is_favorite': fields.Boolean
}

status_fields = {
    'url': fields.String,
    'state': fields.String(attribute='state.name'),
    'title': fields.String,
    'name': fields.String,
    'volume': fields.Integer,
    'bitrate': fields.String,
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('url', type=str)
parser.add_argument('is_favorite', type=bool)

class StationResource(Resource):

    @marshal_with(station_fields)
    def get(self, id):
        # Get
        station = db.session.query(Station).filter(Station.id == id).first()
        if not station:
            abort(404, message="Station {} doesn't exist".format(id))
        return station


    @marshal_with(station_fields)
    def put(self, id):
        # Update
        parsed_args = parser.parse_args()
        station = db.session.query(Station).filter(Station.id == id).first()
        if not station:
            abort(404, message="Station {} doesn't exist".format(id))

        station.name = parsed_args['name']
        station.url = parsed_args['url']
        station.is_favorite = parsed_args['is_favorite']

        try:
            db.session.add(station)
            db.session.commit()
        except:
            db.session.rollback()
            raise

        return station, 201

    def delete(self, id):
        station = db.session.query(Station).filter(Station.id == id).first()
        if not station:
            abort(404, message="Station {} doesn't exist".format(id))

        try:
            db.session.delete(station)
            db.session.commit()
        except:
            db.session.rollback()
            raise

        return {}, 204

class StationListResource(Resource):

    @marshal_with(station_fields)
    def get(self):
        # Get
        parsed_args = parser.parse_args()
        if parsed_args['is_favorite']:
            stations = db.session.query(Station).filter(Station.is_favorite == parsed_args['is_favorite']).all()
        else:
            stations = db.session.query(Station).all()
        return stations


    @marshal_with(station_fields)
    def post(self):
        # Create
        parsed_args = parser.parse_args()
        station = Station()
        station.name = parsed_args['name']
        station.url = parsed_args['url']
        station.is_favorite = parsed_args['is_favorite']

        try:
            db.session.add(station)
            db.session.commit()
        except:
            db.session.rollback()
            raise

        return station, 201

class StatusResource(Resource):

    def __init__(self, radio):
        self.radio = radio


    @marshal_with(status_fields)
    def get(self):
        return self.radio.get_status()
