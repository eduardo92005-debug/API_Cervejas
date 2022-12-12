from flask_restful import Resource
from src import api

class BeerList(Resource):
    def get(self):
        return 'Ola mundo'

api.add_resource(BeerList, '/beers')