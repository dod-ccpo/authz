def map_config(config):
    return {
        'ENV': config['default']['ENVIRONMENT'],
        'DEBUG': config['default']['DEBUG'],
        'SQLALCHEMY_DATABASE_URI': config['default']['DATABASE_URI'],
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }
