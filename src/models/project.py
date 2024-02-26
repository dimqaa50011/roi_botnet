from typing import Optional

import ormar

from .base_model import BaseModel
from .chat import Chat
from .bot import Bot


class Project(BaseModel):

    title: str = ormar.String(max_length=64)
    from_chat: Chat = ormar.ForeignKey(Chat)
    to_chat: Chat = ormar.ForeignKey(Chat)
    bots: Optional[list[Bot]] = ormar.ManyToMany(
        Bot, related_name="bots_project"
    )

    class Meta:
        tablename: str = "project"
