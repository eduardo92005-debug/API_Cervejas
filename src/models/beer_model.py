from src import db
from datetime import datetime

class BestTemperatureBeers(db.Model):
    __tablename__ = 'BestTemperatureBeers'
    id_best_beer_temperature = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    style_beer = db.Column(db.String(30))
    min_best_temperature = db.Column(db.Integer)
    max_best_temperature = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.Date)


class Beers(db.Model):
    __tablename__ = 'Beers'
    id_beer = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    style_beer = db.Column(db.String(30))
    id_best_beer_temperature = db.Column(db.Integer,db.ForeignKey('BestTemperatureBeers.id_best_beer_temperature', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.Date)