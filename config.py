DEBUG = True
USERNAME = 'root'
PASSWORD = 'edu102030'
SERVER = 'localhost'
DB = 'beer_api'
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
