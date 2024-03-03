from dataclasses import dataclass


@dataclass
class DbConfig:
    schema: str
    db_user: str
    db_passwd: str
    db_host: str
    db_port: str
    db_name: str

    @property
    def uri(self):
        return "{schema}://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}".format(
            schema=self.schema, db_user=self.db_user, db_passwd=self.db_passwd,
            db_host=self.db_host, db_port=self.db_port, db_name=self.db_name
        )
