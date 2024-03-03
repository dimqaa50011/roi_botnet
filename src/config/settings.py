from dataclasses import dataclass

from .db_conf import DbConfig
from .mongo_conf import MongoConfig


@dataclass
class AppSettings:
    db_conf: DbConfig
    # mongo_conf: MongoConfig
