DEBUG = True
USERNAME = 'testeroot'
PASSWORD = 'teste'
SERVER = 'localhost'
DB = 'beer_api'
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True