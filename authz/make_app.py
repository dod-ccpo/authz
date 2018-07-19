import os
from flask import Flask
from configparser import ConfigParser

from authz.config import map_config
from authz.database import db
from authz.serializers import marshmallow


def make_app(config):
    app = Flask(__name__)
    app.config.update(config)

    db.init_app(app)
    marshmallow.init_app(app)

    # Imported at the end to avoid circular imports.
    from authz.api import api

    app.register_blueprint(api, url_prefix="/api/v1/")

    return app


def make_config():
    BASE_CONFIG_FILENAME = os.path.join(os.path.dirname(__file__), "../config/base.ini")
    ENV_CONFIG_FILENAME = os.path.join(
        os.path.dirname(__file__),
        "../config/",
        "{}.ini".format(os.getenv("FLASK_ENV", "dev").lower()),
    )
    OVERRIDE_CONFIG_FILENAME = os.getenv("OVERRIDE_CONFIG_FULLPATH")

    config = ConfigParser()

    config_files = [BASE_CONFIG_FILENAME, ENV_CONFIG_FILENAME]
    if OVERRIDE_CONFIG_FILENAME:
        config_files.append(OVERRIDE_CONFIG_FILENAME)

    # ENV_CONFIG will override values in BASE_CONFIG
    # OVERRIDE_CONFIG will override values in ENV_CONFIG or BASE_CONFIG
    config.read(config_files)

    # Assemble DATABASE_URI value
    database_uri = ('postgres://'
                   + config.get('default', 'DATABASE_USERNAME')
                   + ':'
                   + config.get('default', 'DATABASE_PASSWORD')
                   + '@'
                   + config.get('default', 'DATABASE_HOST')
                   + ':'
                   + config.get('default', 'DATABASE_PORT')
                   + '/'
                   + config.get('default', 'DATABASE_NAME'))
    config.set('default', 'DATABASE_URI', database_uri)

    return map_config(config)
