from flask_restful import Resource
from flask import jsonify, make_response
from src import api
from ..services import beer_service
from ..schemas import beer_schema

class BeerList(Resource):
    def get(self):
        beers = beer_service.list_beers()
        bs = beer_schema.BeerSchema(many=True)
        return make_response(bs.jsonify(beers),200)

api.add_resource(BeerList, '/beers')