import databases
import sqlalchemy

import ormar

database = databases.Database("")  # заполнить конфиги
metadata = sqlalchemy.MetaData()


class BaseModel(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.BigInteger(primary_key=True)
