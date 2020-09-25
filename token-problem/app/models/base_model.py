from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy, models_committed
from flask_migrate import Migrate


migrate = Migrate()
ma = Marshmallow()
db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    created_on = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated_on = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)