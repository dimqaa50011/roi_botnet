from abc import ABC, abstractmethod


class BaseController(ABC):

    @abstractmethod
    async def create(
            self,
            *args,
            **kwargs
            ):
        pass

    @abstractmethod
    async def delete(
            self,
            *args,
            **kwargs
            ):
        pass

    @abstractmethod
    async def update(
            self,
            *args,
            **kwargs
            ):
        pass

    @abstractmethod
    async def get_one(
            self,
            *args,
            **kwargs
            ):
        pass

    @abstractmethod
    async def get_many(
            self,
            *args,
            **kwargs
            ):
        pass
    