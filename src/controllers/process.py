from .base import BaseController

from src.models.process import Process
from src.models.chat import Chat
from src.models.bot import Bot


class ProcessController(BaseController):

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
            type_process: str,
            status: str,
            from_chat_id: int,
            to_chat_id: int,
            bots_id: list[int]
            ):
        from_chat: Chat = await self.get_chat(from_chat_id)
        to_chat: Chat = await self.get_chat(to_chat_id)
        bots_list: list[Bot] = await self.get_bots(bots_id)

        process: Process = await Process.objects.create(
            type_process=type_process,
            status=status,
            from_chat=from_chat,
            to_chat=to_chat,
            bots=bots_list
        )
        # TODO: разобраться с полем bots M2M
        return process

    async def delete(
            self,
            process_id: int
            ):
        await Process.objects.delete(id=process_id)

    async def get_one(
            self,
            process_id: int
            ) -> Process:
        process: Process = await Process.objects.get_or_none(id=process_id)
        return process

    async def get_many(self) -> list[Process]:
        process_list: list[Process] = await Process.objects.all()
        return process_list

    async def update(self, *args, **kwargs):
        return await super().update(*args, **kwargs)
    