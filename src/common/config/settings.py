from dataclasses import dataclass

from .db_conf import DbConfig


@dataclass
class AppSettings:
    db_conf: DbConfig
