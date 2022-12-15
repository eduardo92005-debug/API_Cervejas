from flask_restful import Resource
from flask import jsonify, make_response, request
from src import api
from ..handlers import requests_handlers
from ..repositories import beer_repository
from ..schemas import beer_schema
from ..entitys import beer_entity
from ..services import beer_service, beer_temperature_service


class BeerList(Resource):
    def get(self):
        """
            Returns all beers in the database
            ---
            tags:
                - Beers
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

    def post(self):
        """
            Insert a new beer in the database
            ---
            tags:
                - Beers
            parameters:
                - in: body
                  name: beers
                  description: The beer to insert
                  schema:
                    id: beer
                    properties:
                        style_beer:
                            type: string
                            description: The beer style
                        id_best_beer_temperature:
                            type: integer
                            description: The beer best temperature id
            responses:
                201:
                    description: The beer was inserted
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
                400:
                    description: The beer was not inserted
                    schema:
                        id: error
                        properties:
                            style_beer:
                                type: string
                                description: The beer style
                            id_best_beer_temperature:
                                type: integer
                                description: The beer best temperature id
                500:
                    description: The beer was not inserted, internal server error
        """
        bs = beer_schema.BeerSchema()
        validate = bs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            try:
                style_beer = request.json["style_beer"]
                id_best_beer_temperature = request.json["id_best_beer_temperature"]
                check_id_beer_temp = beer_repository.list_beer_temperature_by_id(
                    id_best_beer_temperature)
                if check_id_beer_temp is None:
                    return make_response("The id_best_beer_temperature passed does not exist in the database", 404)
                else:
                    new_beer = beer_entity.Beer(
                        style_beer, id_best_beer_temperature)
                    result = beer_service.insert_beer(new_beer)
                    return make_response(bs.jsonify(result), 201)
            except Exception as e:
                return make_response("Check if the data was passed correctly or a bad code: " + str(e), 500)


class BeerTemperatureList(Resource):
    def get(self):
        """
            Returns all beers with average temperature
            ---
            tags:
                - Beers temperature
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

    def post(self):
        """
            Insert a new beer temperature in the database
            ---
            tags:
                - Beers temperature
            parameters:
                - in: body
                  name: beers
                  description: The beer temperature to insert
                  schema:
                    id: beer
                    properties:
                        style_beer:
                            type: string
                            description: The beer style
                        min_best_temperature:
                            type: integer
                            description: The beer min best temperature
                        max_best_temperature:
                            type: integer
                            description: The beer max best temperature 
            responses:
                201:
                    description: The beer temperature was inserted
                    schema:
                        id: beer
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
                            created_at:
                                type: string
                                description: The beer creation date
                            updated_at: 
                                type: string
                                description: The beer update date
                400:
                    description: The beer temperature was not inserted
                    schema:
                        id: error
                        properties:
                            style_beer:
                                type: string
                                description: The beer style
                            min_best_temperature:
                                type: integer
                                description: The beer min best temperature
                            max_best_temperature:
                                type: integer
                                description: The beer max best temperature
                500:
                    description: The beer temperature was not inserted, internal server error
        """
        bs = beer_schema.BestBeerTemperatureSchemaAll()
        validate = bs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            try:
                style_beer = request.json["style_beer"]
                min_best_temperature = request.json["min_best_temperature"]
                max_best_temperature = request.json["max_best_temperature"]
                new_beer = beer_entity.BeerTemperatureEntity(
                    style_beer, min_best_temperature, max_best_temperature)
                result = beer_temperature_service.insert_beer_temperature(
                    new_beer)
                return make_response(bs.jsonify(result), 201)
            except Exception as e:
                return make_response("Check if the data was passed correctly or a bad code: " + str(e), 500)




class BeerDetail(Resource):
    def get(self, id):
        """
            Returns a beer by id
            ---
            tags:
                - Beers
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
            return make_response(jsonify("Beer ID not found"), 404)
        else:
            bs = beer_schema.BeerSchema()
            return make_response(bs.jsonify(beer), 200)

    def put(self, id):
        """
            Update a beer by id
            ---
            tags:
                - Beers
            parameters:
                - in: path
                  name: id
                  type: integer
                  required: true
                  description: The beer id
                - in: body
                  name: beers
                  description: The beer to update
                  schema:
                    id: beer
                    properties:
                        style_beer:
                            type: string
                            description: The beer style
                        id_best_beer_temperature:
                            type: integer
                            description: The beer best temperature id
            responses:
                200:
                    description: The beer was updated
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
                400:
                    description: The beer was not updated
                    schema:
                        id: error
                        properties:
                            style_beer:
                                type: string
                                description: The beer style
                            id_best_beer_temperature:
                                type: integer
                                description: The beer best temperature id
                404:
                    description: The beer was not found
                500:
                    description: The beer was not updated, internal server error
        """
        beer = beer_repository.list_beer_by_id(id)
        if beer is None:
            return make_response(jsonify("Beer ID not found"), 404)
        else:
            bs = beer_schema.BeerSchema()
            validate = bs.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                try:
                    id_beer = id
                    style_beer = request.json["style_beer"]
                    id_best_beer_temperature = request.json["id_best_beer_temperature"]
                    check_id_beer_temp = beer_repository.list_beer_temperature_by_id(id_best_beer_temperature)
                    if check_id_beer_temp is None:
                        return make_response("The id_best_beer_temperature passed does not exist in the database", 404)
                    else:
                        beer.id_beer = id_beer
                        beer.style_beer = style_beer
                        beer.id_best_beer_temperature = id_best_beer_temperature
                        result = beer_service.update_beer(beer)
                        return make_response(bs.jsonify(result), 200)
                except Exception as e:
                    return make_response("Check if the data was passed correctly or a bad code: " + str(e), 500)



    def delete(self, id):
        """
            Delete a beer by id
            ---
            tags:
                - Beers
            parameters:
                - in: path
                  name: id
                  type: integer
                  required: true
                  description: The beer id
            responses:
                204:
                    description: The beer was deleted, no content to show
                404:
                    description: The beer was not found
        """
        beer = beer_repository.list_beer_by_id(id)
        if beer is None:
            return make_response(jsonify("Beer ID not found"), 404)
        else:
            result = beer_service.delete_beer(beer)
            return make_response('', 204)


class BeerTemperatureDetail(Resource):
    def get(self, id):
        """
            Returns a beer temperature by id
            ---
            tags:
                - Beers temperature
            parameters:
                - in: path
                  name: id
                  type: integer
                  required: true
                  description: The beer temperature id
            responses:
                200:
                    description: The beer temperature
                    schema:
                        id: beer_temperature
                        properties:
                            id_best_beer_temperature:
                                type: integer
                                description: The beer temperature id
                            min_best_temperature:
                                type: integer
                                description: The beer min temperature
                            max_best_temperature:
                                type: integer
                                description: The beer max temperature
                            created_at:
                                type: string
                                description: The beer temperature creation date
                            updated_at:
                                type: string
                                description: The beer temperature update date
                404:
                    description: The beer temperature id was not found

        """
        beer = beer_repository.list_beer_temperature_by_id(id)
        if beer is None:
            return make_response(jsonify("Beer Temperature ID not found"), 404)
        else:
            bs = beer_schema.BestBeerTemperatureSchemaAll()
            beer.average = (beer.max_best_temperature + beer.min_best_temperature) / 2
            return make_response(bs.jsonify(beer), 200)
    
    def put(self,id):
        """
            Update a beer temperature by id
            ---
            tags:
                - Beers temperature
            parameters:
                - in: path
                  name: id
                  type: integer
                  required: true
                  description: The beer temperature id
                - in: body
                  name: beer_temperature
                  description: The beer temperature to update
                  schema:
                        id: beer_temperature
                        properties:
                            style_beer:
                                type: string
                                description: The beer style
                            max_best_temperature:
                                type: integer
                                description: The beer max temperature
                            min_best_temperature:
                                type: integer
                                description: The beer min temperature
            responses:
                200:
                    description: The beer temperature was updated
                    schema:
                        id: beer_temperature
                        properties:
                            id_best_beer_temperature:
                                type: integer
                                description: The beer temperature id
                            style_beer:
                                type: string
                                description: The beer style
                            max_best_temperature:
                                type: integer
                                description: The beer max temperature
                            min_best_temperature:
                                type: integer
                                description: The beer min temperature
                            created_at:
                                type: string
                                description: The beer temperature creation date
                            updated_at:
                                type: string
                                description: The beer temperature update date
                400:
                    description: The beer temperature was not updated, bad request
                404:
                    description: The beer temperature id was not found
                500:
                    description: The beer temperature was not updated, internal server error
        """
        id_best_beer_temperature = id
        beer = beer_repository.list_beer_temperature_by_id(id_best_beer_temperature)
        if beer is None:
            return make_response(jsonify("Best Beer Temperature ID not found"), 404)
        else:
            bs = beer_schema.BestBeerTemperatureSchemaAll()
            validate = bs.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                try:
                    style_beer = request.json["style_beer"]
                    max_best_temperature = request.json["max_best_temperature"]
                    min_best_temperature = request.json["min_best_temperature"]
                    beer.id_beer = id_best_beer_temperature
                    beer.style_beer = style_beer
                    beer.max_best_temperature = max_best_temperature
                    beer.min_best_temperature = min_best_temperature
                    result = beer_temperature_service.update_beer_temperature(beer)
                    return make_response(bs.jsonify(result), 200)
                except Exception as e:
                    return make_response("Check if the data was passed correctly or a bad code: " + str(e), 500)

    def delete(self,id):
        """
            Delete a beer temperature by id
            ---
            tags:
                - Beers temperature
            parameters:
                - in: path
                  name: id
                  type: integer
                  required: true
                  description: The beer temperature id
            responses:
                204:
                    description: The beer temperature was deleted, no content to show
                404:
                    description: The beer temperature id was not found
        """
        id_best_beer_temperature = id
        beer = beer_repository.list_beer_temperature_by_id(id_best_beer_temperature)
        if beer is None:
            return make_response(jsonify("Best Beer Temperature ID not found"), 404)
        else:
            result = beer_temperature_service.delete_beer_temperature(beer)
            return make_response('', 204)


class BeerTemperaturePlaylistList(Resource):
    def get(self):
        """
            Returns a beer by temperature and a playlist related with them
            ---
            tags:
                - Beers temperature
            parameters:
                - in: body
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
        temperature = request.json["temperature"]
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
api.add_resource(BeerTemperaturePlaylistList, '/beers/temperature/playlist')
api.add_resource(BeerTemperatureList, '/beers/temperature')
api.add_resource(BeerTemperatureDetail, '/beers/temperature/<int:id>')
