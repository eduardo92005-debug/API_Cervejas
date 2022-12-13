from sqlalchemy import text
from ..utils import dict_utils
from src import db

def get_average_table_temperature():
    sql_text = text("SELECT * FROM avg_temp_beers")
    response = db.session.execute(sql_text)
    return response

def get_nearest_value_from_temperature(temperature_input):
    average_table = get_average_table_temperature()
    dict_distance = {}
    for i in average_table:
        distance = abs(temperature_input - i.average)
        dict_distance[i.id_best_beer_temperature] = distance
    value_min_distance = min(dict_distance.values())
    #Get ID from beers that has the nearest value to the input
    list_key_min_distance = dict_utils.get_key_dict(dict_distance, value_min_distance)
    return list_key_min_distance

