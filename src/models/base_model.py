import databases
import sqlalchemy

import ormar

from src.config import app_settings

database = databases.Database(app_settings.db_conf.uri)
metadata = sqlalchemy.MetaData()


class BaseModel(ormar.Model):
    class Meta:
        database = database
        abstract = True
        metadata = metadata

    id: int = ormar.BigInteger(primary_key=True)
