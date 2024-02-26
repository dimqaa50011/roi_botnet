import ormar

from .base_model import BaseModel
from .parsing_filters import ParsingFilters
from .process import Process


class InviterConfig(BaseModel):

    size_chunk: int = ormar.Integer()
    pause: int = ormar.Integer()
    timeout: int = ormar.Integer()
    all_chunk: bool = ormar.Boolean()

    class Meta:
        tablename: str = "inviter_config"


class Config(BaseModel):

    filter: ParsingFilters = ormar.ForeignKey(ParsingFilters)
    inviter_config: InviterConfig = ormar.ForeignKey(InviterConfig)
    process: Process
