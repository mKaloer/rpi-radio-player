from flask_restful import Resource, fields, marshal_with, abort, reqparse


category_fields = {
    'id': fields.Integer(),
    'title': fields.String(),
    'description': fields.String(),
}
# Add recursive definition
category_fields['children'] = fields.List(fields.Nested(category_fields))

country_fields = {
    'name': fields.String(),
    'code': fields.String(),
    'region': fields.String(),
    'subregion': fields.String()
}

station_fields = {
    'id': fields.Integer(),
    'name': fields.String(),
    'country': fields.String(),
    'image': {
        'url': fields.String(),
        'thumb': fields.String()
    },
    'streams': fields.List(fields.Nested(
        {
            'url': fields.String(),
            'bitrate': fields.Integer(),
            'content_type': fields.String(),
            'status': fields.Integer(),
        }
    )),
    'categories': fields.List(fields.Nested(category_fields))
}

class CategoryListResource(Resource):

    def __init__(self, discover_provider):
        self.discover_provider = discover_provider

    @marshal_with(category_fields)
    def get(self):
        # Get
        return self.discover_provider.get_categories()


class CategoryStationListResource(Resource):

    def __init__(self, discover_provider):
        self.discover_provider = discover_provider

    @marshal_with(station_fields)
    def get(self, id):
        # Get
        return self.discover_provider.get_stations_in_category(id)

class CountryStationListResource(Resource):

    def __init__(self, discover_provider):
        self.discover_provider = discover_provider

    @marshal_with(station_fields)
    def get(self, country_code):
        # Get
        return self.discover_provider.get_stations_in_country(country_code)


class CountryListResource(Resource):

    def __init__(self, discover_provider):
        self.discover_provider = discover_provider

    @marshal_with(country_fields)
    def get(self):
        # Get
        return self.discover_provider.get_countries()
