# services/users/project/__init__.py


import os

from flask import Flask  # nuevo
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS  # nuevo
from flask_migrate import Migrate  # nuevo
from flask_bcrypt import Bcrypt  # nuevo

# instantiate the db
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
cors = CORS()  # nuevo
migrate = Migrate()  # nuevo
bcrypt = Bcrypt()  # nuevo


# nuevo
def create_app(script_info=None):

    # instanciado la  app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # configurar la extension
    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app)  # nuevo
    migrate.init_app(app, db)  # nuevo
    bcrypt.init_app(app)  # nuevo

    # registrar blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    from project.api.auth import auth_blueprint  # nuevo
    app.register_blueprint(auth_blueprint)       # nuevo

    # contexto shell para flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app


# import os
# from flask import Flask, jsonify
# from flask_restful import Resource, Api
# from flask_sqlalchemy import SQLAlchemy

# instantiate the app
# app = Flask(__name__)

# api = Api(app)

# @app.route('/users/ping', methods=['GET'])

# establelciendo configuracion
# app.config.from_object('project.config.DevelopmentConfig')
# app_settings = os.getenv('APP_SETTINGS')
# app.config.from_object(app_settings)

# instanciado la db
# db = SQLAlchemy(app)  # nuevo

# modelo
# class User(db.Model):  # nuevo
#    __tablename__ = "users"
#    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    username = db.Column(db.String(128), nullable=False)
#    email = db.Column(db.String(128), nullable=False)
#    active = db.Column(db.Boolean(), default=True, nullable=False)

#    def __init__(self, username, email):
#        self.username = username
#        self.email = email


# class UsersPing(Resource):
#    def get(self):
#        return {
#        'status': 'success',
#        'message': 'pong!'
#    }


# import sys
# print(app.config, file=sys.stderr)

# api.add_resource(UsersPing, '/users/ping')
