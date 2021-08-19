from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api

from users.apis import api as users_api


db = SQLAlchemy()
migrate = Migrate()
api = Api(
    version='1.0', 
    title='Flask Migration POC', 
    description='simple POC for flask db migrations',
)

api.add_namespace(users_api)