from src.botnet.base.runner import BaseRunner


class DefaultRunner(BaseRunner):
    async def start_process(self, *args, **kwargs):
        ...
