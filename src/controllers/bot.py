import os

from typing import Optional

from fastapi import UploadFile

from .base import BaseController

from src.models.bot import Bot, BotInfo
from src.models.session import Session


class BotController(BaseController):

    def __write_file_session(self, file_session: UploadFile) -> str:
        file_location: str = f"sessions/{file_session.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file_session.file.read())
        return file_session.filename

    async def _get_path_session(self, file_session: UploadFile) -> str:
        file_name: str = self.__write_file_session(file_session)
        file_path: str = os.path.abspath(file_name)
        return file_path

    async def create(
            self,
            file_session: UploadFile,
            name: str,
            market: bool,
            api_id: Optional[str] = None,
            api_hash: Optional[str] = None,
            phone: Optional[str] = None,
            password: Optional[str] = None
            ):
        file_path: str = await self._get_path_session(file_session)
        session: Session = await Session.objects.create(
            path=file_path,
            api_id=api_id,
            api_hash=api_hash,
            phone=phone,
            password=password,
            market=market
        )
        bot_info: BotInfo = await BotInfo.objects.create()
        bot: Bot = await Bot.objects.create(
            name=name,
            bot_info=bot_info,
            session=session
        )
        return bot

    async def delete(
            self,
            bot_id: int
            ):
        await Bot.objects.delete(id=bot_id)

    async def get_one(
            self,
            bot_id: int
            ) -> Bot | None:
        bot: Bot = await Bot.objects.get_or_none(id=bot_id)
        return bot

    async def get_many(
            self
            ) -> list[Bot]:
        bot_list: list[Bot] = await Bot.objects.all()
        return bot_list

    async def update(self, *args, **kwargs):
        return await super().update(*args, **kwargs)