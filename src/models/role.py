import ormar

from .base_model import BaseModel


class Role(BaseModel):

    name: str = ormar.String(max_length=32)
    add_operator: str = ormar.Boolean()
    add_session: str = ormar.Boolean()
    start_process: str = ormar.Boolean()

    class Meta:
        tablename: str = "role"
