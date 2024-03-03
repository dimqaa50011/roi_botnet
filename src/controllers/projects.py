from typing import Any

from .base import BaseController

from src.models.project import Project
from src.models.chat import Chat
from src.models.bot import Bot


class ProjectController(BaseController):

    async def get_chat(self, chat_id) -> Chat | None:
        chat: Chat = await Chat.objects.get_or_none(id=chat_id)
        return chat

    async def get_bots(self, bots_id: list[int]):
        bot_list: list[Bot] = []
        if bots_id is None:
            return
        for bot_id in bots_id:
            bot: Bot = await Bot.objects.get_or_none(id=bot_id)
            if bot:
                bot_list.append(bot)
        return bot_list

    async def create(
            self,
            title: str,
            from_chats: list[int],
            to_chats: list[int],
            bots: list[int]
            ) -> Project:
        pass
    # TODO: надо обсудить модель project поля from_chats и to_chats, сейчас это FK, можно сделать М2М.

    async def get_many(
            self,
            admin_id: int
            ) -> list[Project]:
        pass

    async def get_one(
            self,
            project_id: int
            ) -> Project:
        pass

    async def delete(
            self,
            project_id: int
            ) -> bool:
        pass

    async def  update(
            self,
            project_id: int,
            data: dict[Any]
            ) -> bool:
        pass