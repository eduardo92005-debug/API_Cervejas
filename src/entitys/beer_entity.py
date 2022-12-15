
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

