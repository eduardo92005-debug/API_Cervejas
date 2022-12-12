from ..models import beer_model
from src import db

def list_beers():
    beers =  beer_model.Beers.query.all()
    return beers

def list_beer_by_id(id):
    beer = beer_model.Beers.query.filter_by(id_beer=id).first()
    return beer

def list_beer_by_temperature(temperature):
    beer = beer_model.BestTemperatureBeers.query.filter_by(max_best_temperature=temperature).first()
    return beer