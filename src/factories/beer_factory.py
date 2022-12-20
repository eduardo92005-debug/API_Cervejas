from faker import Faker
from src import services
import random

class Factory:
    def __init__(self, entity):
        self.__entity = entity 
        self.__fake = Faker()

    @property
    def entity(self):
        return self.__entity
    
    @entity.setter
    def entity(self, entity):
        self.__entity = entity

    def get_attributes_definition(self):
        return [{
            'style_beer': self.__fake.word(),
            'id_best_beer_temperature': random.randint(1,10),
            'created_at': self.__fake.date_time(),
            'updated_at': self.__fake.date_time(),
        }]

    def create(self, quantity=1):
        for i in range(quantity):
            attributes = self.get_attributes_definition()
            services.insert_beer(self.__entity(**attributes))
    
    def create_mock(self, quantity=1):
        beers = []
        for i in range(quantity):
            attributes = self.get_attributes_definition()
            beers.append(*attributes)
        return beers
