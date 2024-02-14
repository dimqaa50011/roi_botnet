import abc


class AbstractBot(abc.ABC):
    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    async def run(self):
        raise NotImplementedError


class BaseTelegramBot(AbstractBot):
    def __init__(self, link: str):
        self._link = link

    async def run(self):
        return await super().run()
