import requests
from requests_cache.core import CachedSession

class DirbleAPI:


    API_BASE_URL = "http://api.dirble.com/v2/"


    def __init__(self, api_key):
        self.api_key = api_key
        self.session = CachedSession(cache_name='dirble_cache', backend='memory', expire_after=600)


    def _request(self, endpoint, params={}):
        url = "{}{}".format(DirbleAPI.API_BASE_URL, endpoint)
        params['token'] = self.api_key
        return self.session.get(url, params=params)


    def get_categories(self):
        r = self._request('categories/tree')
        categories = []
        for cat in r.json():
            categories.append(DirbleAPI._format_category(cat))
        return categories


    def get_stations_in_category(self, category_id):
        r = self._request('category/{}/stations'.format(category_id))
        stations = []
        for station in r.json():
            stations.append(DirbleAPI._format_station(station))
        return stations


    def get_stations_in_country(self, country_code):
        r = self._request('country/{}/stations'.format(country_code))
        stations = []
        for station in r.json():
            stations.append(DirbleAPI._format_station(station))
        return stations


    def get_countries(self):
        r = self._request('countries')
        countries = []
        for country in r.json():
            countries.append(DirbleAPI._format_country(country))
        return countries


    @staticmethod
    def _format_category(category):
        return {
            'id': category['id'],
            'title': category['title'],
            'description': category['description'],
            'children': [DirbleAPI._format_category(cat) for cat in category.get('children', [])]
        }


    @staticmethod
    def _format_country(country):
        return {
            'name': country['name'],
            'code': country['country_code'],
            'region': country['region'],
            'subregion': country['subregion']
        }


    @staticmethod
    def _format_station(station):
        return {
            'id': station['id'],
            'name': station['name'],
            'country': station['country'],
            'image': {
                'url': station['image']['url'],
                'thumb': station['image']['thumb']['url']
            },
            'streams': [
                {
                    'url': stream['stream'],
                    'bitrate': stream['bitrate'],
                    'content_type': stream['content_type'],
                    'status': stream['status']
                } for stream in station['streams']
            ],
            'categories': [DirbleAPI._format_category(cat) for cat in station['categories']]
        }
