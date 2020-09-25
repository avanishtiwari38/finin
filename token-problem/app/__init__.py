import os
from logging.config import dictConfig

from flask import Flask
from flask_restful import Api
from flask import Blueprint

from app.config.celery_config import make_celery, Config
from .models import *

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s.%(funcName)s Line %(lineno)s: %(message)s',
    }},
    'handlers':
        {'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/www/html/token_problem/token-problem/token_problem-app.log',
            'formatter': 'default'
        },
        'celery-file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/www/html/token_problem/token-problem/celery-tasks.log',
            'formatter': 'default'
            }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    },
    'app.tasks.tasks': {
        'level': 'DEBUG',
        'handlers': ['celery-file']
    }
})

# flask app config
flask_app = Flask(__name__, instance_relative_config=True)

flask_app.config.from_object(Config)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

flask_app.register_blueprint(api_bp, url_prefix='/api')

# initialise sqlalchemy
db.init_app(flask_app)
# initialise marshmallow
ma.init_app(flask_app)

# initialise blueprints
api.init_app(api_bp)

# initialise flask migrations
migrate.init_app(flask_app, db)

# initilise celery
celery_obj = make_celery(flask_app)

basedir = os.path.join(flask_app.root_path)
# delibrately added in the end to avoid circular dependencies
from app import urls
