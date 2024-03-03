from typing import Any, Optional

from fastapi import File

from .base import BaseController

from src.models.bot import Bot, BotInfo
from src.models.session import Session

class BotController(BaseController):

    def __write_file_session(self, file_session: Any):
        with open(file_session)


    async def _get_path_session(self, file_session: Any):
        with open(file_session, )

    async def create(
            self,
            file_session: Any,
            name: str,
            market: bool,
            api_id: Optional[str] = None,
            api_hash: Optional[str] = None,
            phone: Optional[str] = None,
            password: Optional[str] = None
            ):

        session: Session = await Session.objects.


        pass

    async def delete(
            self,
            bot_id: int
            ) -> bool:
        pass

    async def get_one(
            self,
            bot_id: int
            ) -> Bot:
        pass

    async def get_many(
            self
            ) -> list[Bot]:
        pass

    async def update(self, *args, **kwargs):
        return await super().update(*args, **kwargs)