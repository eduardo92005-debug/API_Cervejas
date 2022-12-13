from sqlalchemy import text
from src import db

def get_average_table_temperature():
    sql_text = text("SELECT * FROM avg_temp_beers")
    response = db.session.execute(sql_text)
    return response

def get_nearest_value_from_temperature(input):
    average_table = get_average_table_temperature()
    print(average_table)