from src import ma
from ..models import beer_model
from marshmallow import fields

class BeerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = beer_model.Beers
        fields = ("id_beer", "style_beer", "id_best_beer_temperature", "created_at", "updated_at")
    id_beer = fields.Integer(required=True)

class BestBeerTemperatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = beer_model.Beers
        fields = ("id_best_beer_temperature", "style_beer", "min_best_temperature","max_best_temperature", "created_at", "updated_at")
