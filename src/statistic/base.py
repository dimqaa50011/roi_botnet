class BaseStatisticWorker:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    async def get_stat(self, *args, **kwargs):
        raise NotImplementedError
