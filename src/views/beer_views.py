from flask_restful import Resource
from flask import jsonify, make_response
from src import api
from ..handlers import requests_handlers
from ..repositories import beer_repository
from ..schemas import beer_schema


class BeerList(Resource):
    def get(self):
        beers = beer_repository.list_beers()
        bs = beer_schema.BeerSchema(many=True)
        return make_response(bs.jsonify(beers), 200)


class BeerDetail(Resource):
    def get(self, id):
        beer = beer_repository.list_beer_by_id(id)
        if beer is None:
            return make_response(jsonify("Not found"), 404)
        else:
            bs = beer_schema.BeerSchema()
            return make_response(bs.jsonify(beer), 200)

    def put(self, id):
        pass

    def delete(self, id):
        pass



class BeerTemperatureList(Resource):
    def get(self):
        beers = beer_repository.list_all_beer_and_average()
        bs = beer_schema.BestBeerTemperatureSchemaAll(many=True)
        return make_response(bs.jsonify(beers), 200)

class BeerTemperatureDetail(Resource):
    def get(self, temperature):
        beer = beer_repository.list_beer_by_temperature(temperature)
        if beer is None:
            return make_response(jsonify("Not found"), 404)
        else:
            bts = beer_schema.BestBeerTemperatureSchemaOne(many=True)
            bts_json = bts.jsonify(beer)
            json_list = []
            for beer_element in bts_json.json:
                request_response = requests_handlers.request_spotify_service(beer_element["style_beer"])
                related = beer_element | request_response
                json_list.append(related)
            return json_list


api.add_resource(BeerList, '/beers')
api.add_resource(BeerDetail, '/beers/<int:id>')
api.add_resource(BeerTemperatureDetail, '/beers/temperature/<int:temperature>')
api.add_resource(BeerTemperatureList, '/beers/temperature')
