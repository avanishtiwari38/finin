from .base_config import BaseConfig


class Config(BaseConfig):
    LOG_PATH = '/var/www/html/token_problem/token_problem/token_problem-app.log'

    POSTGRES_USER = ''
    POSTGRES_PASSWORD = ''
    POSTGRES_HOST = 'localhost'
    POSTGRES_DATABASE = 'token_problem'
    # SQLALCHEMY_DATABASE_URI = "postgresql://root:root@localhost/token_problem"
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_DATABASE)
    FLASK_DEBUG = True
    FLASK_ENV = "development"

    RABBITMQ_HOST = 'localhost'
    RABBITMQ_PORT = 5672
    RABBITMQ_USER = ''
    RABBITMQ_PASSWORD = ''
    broker_url = 'amqp://localhost//'
    # broker_url = "amqp://{}:{}@{}:{}//".format(RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_HOST, RABBITMQ_PORT)