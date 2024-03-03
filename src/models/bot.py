import datetime

import ormar

from .base_model import BaseModel
from .proxy import Proxy
from .session import Session


class BotInfo(BaseModel):

    created_at: datetime.datetime = ormar.DateTime()
    blocked: datetime.datetime = ormar.DateTime()
    count_invite: int = ormar.Integer()

    class Meta:
        tablename: str = "bot_info"


class Bot(BaseModel):

    name: str = ormar.String(max_length=32)
    bot_info: BotInfo = ormar.ForeignKey(BotInfo, related_name="bot")
    proxy: Proxy = ormar.ForeignKey(Proxy, related_name="proxy")
    session: Session = ormar.ForeignKey(Session, related_name="session")

    class Meta:
        tablename: str = "bot"


