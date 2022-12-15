from ..models import beer_model
from src import db
from datetime import datetime

def insert_beer_temperature(beer):
    beer_bd = beer_model.BestTemperatureBeers(style_beer=beer.style_beer,min_best_temperature=beer.min_best_temperature,max_best_temperature=beer.max_best_temperature)
    db.session.add(beer_bd)
    db.session.commit()
    return beer_bd

def update_beer(beer):
    beer_bd = beer_model.Beers.query.filter_by(id_beer=beer.id_beer).first()
    beer_bd.style_beer = beer.style_beer
    beer_bd.id_best_beer_temperature = beer.id_best_beer_temperature
    beer_bd.updated_at = datetime.utcnow()
    db.session.commit()
    return beer_bd

def delete_beer(beer):
    db.session.delete(beer)
    db.session.commit()