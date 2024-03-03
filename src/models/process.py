from enum import Enum
from typing import Optional

import ormar

from .base_model import BaseModel
from .bot import Bot
from .chat import Chat


# class TypeProcess(Enum, str):
#     ...
#
#
# class Status(Enum, str):
#     ...


class Process(BaseModel):

    type_process: str = ormar.String(max_length=10)
    status: str = ormar.String(max_length=10)
    bots: Optional[list[Bot]] = ormar.ManyToMany(
        Bot, related_name="bots_process"
    )
    from_chat: Chat = ormar.ForeignKey(Chat, related_name="from_chat_process")
    to_chat: Chat = ormar.ForeignKey(Chat, related_name="to_chat_process")

    class Meta:
        tablename: str = "process"
