from flask_restful import Resource
from flask import jsonify, make_response
from src import api
from ..services import beer_service
from ..schemas import beer_schema


class BeerList(Resource):
    def get(self):
        beers = beer_service.list_beers()
        bs = beer_schema.BeerSchema(many=True)
        return make_response(bs.jsonify(beers), 200)


class BeerDetail(Resource):
    def get(self, id):
        beer = beer_service.list_beer_by_id(id)
        if beer is None:
            return make_response(jsonify("Not found"), 404)
        else:
            bs = beer_schema.BeerSchema()
            return make_response(bs.jsonify(beer), 200)

    def put(self, id):
        pass

    def delete(self, id):
        pass


class BeerTemperatureDetail(Resource):
    def get(self, temperature):
        beer = beer_service.list_beer_by_temperature(temperature)
        if beer is None:
            return make_response(jsonify("Not found"), 404)
        else:
            bts = beer_schema.BestBeerTemperatureSchema()
            return make_response(bts.jsonify(beer), 200)


api.add_resource(BeerList, '/beers')
api.add_resource(BeerDetail, '/beers/<int:id>')
api.add_resource(BeerTemperatureDetail, '/beers/temperature/<int:temperature>')
