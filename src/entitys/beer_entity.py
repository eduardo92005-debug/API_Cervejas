
class Beer():
    def __init__(self, style_beer, id_best_beer_temperature):
        self.__style_beer = style_beer
        self.__id_best_beer_temperature = id_best_beer_temperature
        self.__created_at = None
        self.__updated_at = None
    
    @property
    def style_beer(self):
        return self.__style_beer

    @style_beer.setter
    def style_beer(self, style_beer):
        self.__style_beer = style_beer
    
    @property
    def id_best_beer_temperature(self):
        return self.__id_best_beer_temperature
    @id_best_beer_temperature.setter
    def id_best_beer_temperature(self, id_best_beer_temperature):
        self.__id_best_beer_temperature = id_best_beer_temperature

    @property
    def created_at(self):
        return self.__created_at
    
    @property
    def updated_at(self):
        return self.__updated_at
    
    @updated_at.setter
    def updated_at(self, updated_at):
        self.__updated_at = updated_at


class BeerTemperatureEntity():
    def __init__(self, style_beer, min_best_temperature, max_best_temperature):
        self.__style_beer = style_beer
        self.__min_best_temperature = min_best_temperature
        self.__max_best_temperature = max_best_temperature
        self.__created_at = None
        self.__updated_at = None
        self._validate()
        
    def _validate(self):
        if self.__min_best_temperature > self.__max_best_temperature:
            raise Exception('Min temperature is greater than max temperature')
    
    @property
    def style_beer(self):
        return self.__style_beer
    
    @style_beer.setter
    def style_beer(self, style_beer):
        self.__style_beer = style_beer

    @property
    def min_best_temperature(self):
        return self.__min_best_temperature

    @min_best_temperature.setter
    def min_best_temperature(self, min_best_temperature):
        self.__min_best_temperature = min_best_temperature
        self._validate()
    
    @property
    def max_best_temperature(self):
        return self.__max_best_temperature

    @max_best_temperature.setter
    def max_best_temperature(self, max_best_temperature):
        self.__max_best_temperature = max_best_temperature
        self._validate()
    
    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at
    
    @updated_at.setter
    def updated_at(self, updated_at):
        self.__updated_at = updated_at


