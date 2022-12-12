from ..models import beer_model
from src import db

def list_beers():
    beers =  beer_model.Beers.query.all()
    return beers