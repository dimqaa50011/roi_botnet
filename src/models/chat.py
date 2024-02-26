from enum import Enum

import ormar

from .base_model import BaseModel


class ChatRestriction(BaseModel):

    is_restricted: bool = ormar.Boolean()
    is_scam: bool = ormar.Boolean()
    is_fake: bool = ormar.Boolean()

    class Meta:
        tablename: str = "chat_restrictions"


class ChatType(Enum, str):
    ...


class Chat(BaseModel):

    chat_type = ormar.Enum(ChatType)
    chat_id: int = ormar.BigInteger()
    link: str = ormar.String(max_length=100)
    linked_chat: str = ormar.String(max_length=100)
    chat_restrictions: ChatRestriction = ormar.ForeignKey(ChatRestriction)
    member_count: int = ormar.BigInteger()
    can_invite_users: bool = ormar.Boolean()
    can_send_messages: bool = ormar.Boolean()

    class Meta:
        tablename: str = "chat"
