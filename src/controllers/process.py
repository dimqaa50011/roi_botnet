from typing import Any

from .base import BaseController

from src.models.process import Process

class ProcessController(BaseController):

    async def create(
            self,
            file_session: Any
            ):
        pass

    async def delete(
            self,
            process_id: int
            ) -> bool:
        pass

    async def get_one(
            self,
            process_id: int
            ) -> Process:
        pass

    async def get_many(self) -> list[Process]:
        pass

    async def update(self, *args, **kwargs):
        return await super().update(*args, **kwargs)
    