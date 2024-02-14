import abc


class AbstructBaseRunner(abc.ABC):
    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    async def start_process(self, *args, **kwargs):
        raise NotImplementedError


class BaseRunner(AbstructBaseRunner):

    def __init__(self, from_chat: str, to_chat: str):
        self._from_chat = from_chat
        self._to_chat = to_chat

    async def start_process(self, *args, **kwargs):
        return await super().start_process(*args, *kwargs)
