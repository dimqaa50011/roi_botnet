import ormar

from .base_model import BaseModel


class Session(BaseModel):

    path: str = ormar.String(max_length=1024)
    api_id: str = ormar.String(max_length=100, nullable=True)
    api_hash: str = ormar.String(max_length=100, nullable=True)
    phone: str = ormar.String(max_length=16, nullable=True)
    password: str = ormar.String(max_length=64, nullable=True)
    market: str = ormar.Boolean()

    class Meta:
        tablename: str = "session"
        