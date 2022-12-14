from flask_restful import Resource
from flask import jsonify, make_response
from src import api
from ..handlers import requests_handlers
from ..repositories import beer_repository
from ..schemas import beer_schema


class BeerList(Resource):
    def get(self):
        """
            Returns all beers in the database
            ---
            tags:
                - beers
            responses:
                200:
                    description: The list of beers
                    schema:
                        id: beers
                        properties:
                            id_beer:
                                type: integer
                                description: The beer id
                            style_beer:
                                type: string
                                description: The beer style
                            id_best_beer_temperature:
                                type: integer
                                description: The beer best temperature id
                            created_at:
                                type: string
                                description: The beer creation date
                            updated_at:
                                type: string
                                description: The beer update date
        """
        beers = beer_repository.list_beers()
        bs = beer_schema.BeerSchema(many=True)
        return make_response(bs.jsonify(beers), 200)


class BeerDetail(Resource):
    def get(self, id):
        """
            Returns a beer by id
            ---
            tags:
                - beers
            parameters:
                - in: path
                  name: id
                  type: integer
                  required: true
                  description: The beer id
            responses:
                200:
                    description: The beer
                    schema:
                        id: beer
                        properties:
                            id_beer:
                                type: integer
                                description: The beer id
                            style_beer:
                                type: string
                                description: The beer style
                            id_best_beer_temperature:
                                type: integer
                                description: The beer best temperature id
                            created_at:
                                type: string
                                description: The beer creation date
                            updated_at:
                                type: string
                                description: The beer update date
                404:
                    description: The beer was not found
        """
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
        """
            Returns all beers with average temperature
            ---
            tags:
                - beers
            responses:
                200:
                    description: The list of beers
                    schema:
                        id: beers
                        properties:
                            id_best_beer_temperature:
                                type: integer
                                description: The beer best temperature id
                            style_beer:
                                type: string
                                description: The beer style
                            min_best_temperature:
                                type: integer
                                description: The beer min best temperature
                            max_best_temperature:
                                type: integer
                                description: The beer max best temperature
                            average:
                                type: integer
                                description: The beer average temperature
                            created_at:
                                type: string
                                description: The beer creation date
                            updated_at:
                                type: string
                                description: The beer update date
        """
        beers = beer_repository.list_all_beer_and_average()
        bs = beer_schema.BestBeerTemperatureSchemaAll(many=True)
        return make_response(bs.jsonify(beers), 200)

class BeerTemperatureDetail(Resource):
    def get(self, temperature):
        """
            Returns a beer by temperature and a playlist related with them
            ---
            tags:
                - beers
            parameters:
                - in: path
                  name: temperature
                  type: integer
                  required: true
                  description: The beer temperature
            responses:
                200:
                    description: The beer and a playlist
                    schema:
                        id: playlist
                        properties:
                            input_beer:
                                type: string
                                description: the input beer in the path
                            name:
                                type: string
                                description: the playlist name
                            tracks:
                                type: array
                                description: the playlist tracks
                                artist:
                                    type: string
                                    description: the track artist
                                name:
                                    type: string
                                    description: the track name
                                link:
                                    type: string
                                    description: the track link
                            style_beer:
                                type: string
                                description: The beer style
                404:
                    description: The beer was not found
                Error:
                    description: The spotify service is not available, check bearer token                  
        """
        beer = beer_repository.list_beer_by_temperature(temperature)
        if beer is None:
            return make_response(jsonify("Not found"), 404)
        else:
            bts = beer_schema.BestBeerTemperatureSchemaOne(many=True)
            bts_json = bts.jsonify(beer)
            json_list = []
            for beer_element in bts_json.json:
                request_response = requests_handlers.request_spotify_service(beer_element["style_beer"])
                related = request_response | beer_element
                json_list.append(related)
            return make_response(json_list,200)


api.add_resource(BeerList, '/beers')
api.add_resource(BeerDetail, '/beers/<int:id>')
api.add_resource(BeerTemperatureDetail, '/beers/temperature/<int:temperature>')
api.add_resource(BeerTemperatureList, '/beers/temperature')
