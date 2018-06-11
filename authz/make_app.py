import os
from flask import Flask
from configparser import ConfigParser

from authz.config import map_config
from authz.database import db
from authz.serializers import marshmallow
from authz.seed_db import seed_db

def make_app(config):
    app = Flask(__name__)
    app.config.update(config)

    db.init_app(app)
    marshmallow.init_app(app)

    seed_db(app, db)

    # Imported at the end to avoid circular imports.
    from authz.api import api
    app.register_blueprint(api)

    return app


def make_config():
    BASE_CONFIG_FILENAME = os.path.join(
        os.path.dirname(__file__),
        '../config/base.ini',
    )
    ENV_CONFIG_FILENAME = os.path.join(
        os.path.dirname(__file__),
        '../config/',
        '{}.ini'.format(os.getenv('FLASK_ENV', 'dev').lower())
    )
    config = ConfigParser()

    # ENV_CONFIG will override values in BASE_CONFIG.
    config.read([BASE_CONFIG_FILENAME, ENV_CONFIG_FILENAME])
    return map_config(config)
