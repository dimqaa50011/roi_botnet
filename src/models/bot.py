import datetime

import ormar

from .base_model import BaseModel
from .proxy import Proxy


class BotInfo(BaseModel):

    created_at: datetime.datetime = ormar.DateTime()
    blocked: datetime.datetime = ormar.DateTime()
    count_invite: int = ormar.Integer()

    class Meta:
        tablename: str = "bot_info"


class Bot(BaseModel):

    api_id: str = ormar.String(max_length=100)
    api_hash: str = ormar.String(max_length=100)
    name: str = ormar.String(max_length=32)
    phone: str = ormar.String(max_length=16)
    bot_info: BotInfo = ormar.ForeignKey(BotInfo)
    proxy: Proxy = ormar.ForeignKey(Proxy)

    class Meta:
        tablename: str = "bot"


