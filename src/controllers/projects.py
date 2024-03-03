from typing import Any

from .base import BaseController

from src.models.project import Project



class ProjectController(BaseController):

    async def create(
            self,
            title: str,
            from_chats: list[str],
            to_chats: list[str],
            bots: list[int]
            ) -> Project:
        pass

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