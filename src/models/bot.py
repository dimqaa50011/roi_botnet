import datetime

import ormar

from .base_model import BaseModel
from .proxy import Proxy
from .session import Session


class BotInfo(BaseModel):

    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    blocked: datetime.datetime = ormar.DateTime(nullable=True)
    count_invite: int = ormar.Integer(default=0)

    class Meta:
        tablename: str = "bot_info"


class Bot(BaseModel):

    name: str = ormar.String(max_length=32)
    bot_info: BotInfo = ormar.ForeignKey(BotInfo, related_name="bot")
    proxy: Proxy = ormar.ForeignKey(Proxy, related_name="proxy", nullable=True)
    session: Session = ormar.ForeignKey(Session, related_name="session")

    class Meta:
        tablename: str = "bot"


