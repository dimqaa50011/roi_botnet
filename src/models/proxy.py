from enum import Enum

import ormar

from .base_model import BaseModel


class ProxySchema(Enum, str):
    ...


class Proxy(BaseModel):

    schema = ormar.Enum(ProxySchema)
    ip: str = ormar.String(max_length=32)
    port: str = ormar.String(max_length=32)
    user: str = ormar.String(max_length=32)
    password: str = ormar.String(max_length=32)
    switch_link: str = ormar.String(max_length=100)

    class Meta:
        tablename: str = "proxy"
