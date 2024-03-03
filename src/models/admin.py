import datetime

import ormar

from .base_model import BaseModel

from .role import Role


class Admin(BaseModel):

    tg_id: int = ormar.BigInteger()
    first_name: str = ormar.String(max_length=64)
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    stats: Role = ormar.ForeignKey(Role)

    class Meta:
        tablename: str = "admin"
