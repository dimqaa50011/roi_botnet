import datetime

import ormar

from .base_model import BaseModel

from .user_chat_stats import UserChatStats


class User(BaseModel):

    tg_id: int = ormar.BigInteger()
    first_name: str = ormar.String(max_length=64)
    last_name: str = ormar.String(max_length=64)
    username: str = ormar.String(max_length=64)
    created_at: datetime.datetime = ormar.DateTime()
    language_code: str = ormar.String(max_length=64)
    phone: str = ormar.String(max_length=16)
    is_premium: bool = ormar.Boolean()
    stats: UserChatStats = ormar.ForeignKey(UserChatStats)

    class Meta:
        tablename: str = "user"
