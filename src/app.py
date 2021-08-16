import os
from flask import Flask
from users import users_api


from shared.db import db, migrate



def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    migrate.init_app(app, db)

    # register urls
    app.register_blueprint(users_api, url_prefix='/users')

    # register models
    from users.models import UserModel


    @app.route('/', methods=['GET'])
    def healthz():
        return {'result': True}

    return app