DEBUG = True
USERNAME = 'root'
PASSWORD = 'password'
SERVER = 'db:3306'
DB = 'beer_api'
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True