from ..models import beer_model
from sqlalchemy import text
from sqlalchemy.sql import or_
from src import db
from ..handlers import temperature_handler

def list_beers():
    beers =  beer_model.Beers.query.all()
    return beers

def list_beer_by_id(id):
    beer = beer_model.Beers.query.filter_by(id_beer=id).first()
    return beer

#def list_beer_by_temperature(temperature):
#    beer = beer_model.BestTemperatureBeers.query.filter_by(max_best_temperature=temperature).first()
#    return beer

def list_beer_by_temperature(temperature):
    list_key_nearest_id_beer = temperature_handler.get_nearest_value_from_temperature(temperature)
    first_id = list_key_nearest_id_beer[0]
    beer = db.session.query(beer_model.BestTemperatureBeers).filter(or_(beer_model.BestTemperatureBeers.id_best_beer_temperature == v for v in list_key_nearest_id_beer))
    beer = beer.order_by(beer_model.BestTemperatureBeers.style_beer.asc()).all()
    return beer

def list_beer_temperature_by_id(id):
    beer = beer_model.BestTemperatureBeers.query.filter_by(id_best_beer_temperature=id).first()
    return beer

def list_all_beer_and_average():
    return temperature_handler.get_average_table_temperature()
