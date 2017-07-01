from flask_restful import Resource, fields, marshal_with, abort, reqparse

from models import Setting
import db

settings_fields = {
    'key': fields.String,
    'value': fields.String()
}

parser = reqparse.RequestParser()
parser.add_argument('key', type=str)
parser.add_argument('value', type=str)

class SettingsResource(Resource):

    @marshal_with(settings_fields)
    def get(self, key):
        # Get
        setting = db.session.query(Setting).filter(Setting.key == key).first()
        if not setting:
            abort(404, message="Setting {} doesn't exist".format(key))
        return setting


    @marshal_with(settings_fields)
    def put(self, key):
        # Update
        parsed_args = parser.parse_args()
        setting = db.session.query(Setting).filter(Setting.key == key).first()
        if not setting:
            abort(404, message="Setting {} doesn't exist".format(key))

        setting.value = parsed_args['value']

        try:
            db.session.add(setting)
            db.session.commit()
        except:
            db.session.rollback()
            raise

        return setting, 201

    def delete(self, key):
        setting = db.session.query(Setting).filter(Setting.key == key).first()
        if not setting:
            abort(404, message="Setting {} doesn't exist".format(key))

        try:
            db.session.delete(setting)
            db.session.commit()
        except:
            db.session.rollback()
            raise

        return {}, 204


class SettingsListResource(Resource):

    @marshal_with(settings_fields)
    def get(self):
        # Get
        settings = db.session.query(Setting).all()
        return settings


    @marshal_with(settings_fields)
    def post(self):
        # Create
        parsed_args = parser.parse_args()
        setting = Setting()
        setting.key = parsed_args['key']
        setting.value = parsed_args['value']

        try:
            db.session.add(setting)
            db.session.commit()
        except:
            db.session.rollback()
            raise

        return setting, 201
