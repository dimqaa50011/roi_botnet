from enum import Enum
from typing import Optional

import ormar

from .base_model import BaseModel
from .bot import Bot
from .chat import Chat


class TypeProcess(Enum, str):
    ...


class Status(Enum, str):
    ...


class Process(BaseModel):

    type_process: TypeProcess = ormar.Enum(TypeProcess)
    status: Status = ormar.Enum(Status)
    bots: Optional[list[Bot]] = ormar.ManyToMany(
        Bot, related_name="bots_process"
    )
    from_chat: Chat
    to_chat: Chat

    class Meta:
        tablename: str = "process"
