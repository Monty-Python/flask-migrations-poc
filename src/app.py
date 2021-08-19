import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix


from shared import db, migrate, api


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    
    # register models
    from users.models import UserModel


    @app.route('/healthz', methods=['GET'])
    def healthz():
        return {'result': True}

    return app