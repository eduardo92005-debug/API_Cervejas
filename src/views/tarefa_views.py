from flask_restful import Resource
from src import api

class TarefaList(Resource):
    def get(self):
        return 'Ola mundo'

api.add_resource(TarefaList, '/tarefas')