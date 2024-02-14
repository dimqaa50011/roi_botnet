from dataclasses import dataclass


@dataclass
class MongoConfig:
    user: str
    password: str
    host: str
    port: str
