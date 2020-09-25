from .base_model import *
from .serialiser import BaseSchema


class Token(Base):
    __tablename__ = "token"
    token_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(50), nullable=False, unique=True)
    assigned = db.Column(db.Boolean, default=False)
    expired = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)


class TokenSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Token
        transient = True