from typing import Optional

import ormar

from .base_model import BaseModel

from .chat import Chat
from .bot import BotInfo


class UserChatStats(BaseModel):

    from_chat: Chat = ormar.ForeignKey(Chat, related_name="from_chat_stats")
    to_chat: Chat = ormar.ForeignKey(Chat, related_name="to_chat_stats")
    is_live: bool = ormar.Boolean()
    chat_activity: int = ormar.Integer()
    shared_chats: Optional[list[Chat]] = ormar.ManyToMany(
        Chat, related_name="shared_chats"
    )
    bot_info: BotInfo = ormar.ForeignKey(BotInfo, related_name="bot_info_stats")

    class Meta:
        tablename: str = "user_chat_stats"
