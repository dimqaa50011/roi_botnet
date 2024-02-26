import ormar

from .base_model import BaseModel


class ParsingFilters(BaseModel):

    title: str = ormar.String(max_length=64)
    ...

    class Meta:
        tablename: str = "parsing_filters"
