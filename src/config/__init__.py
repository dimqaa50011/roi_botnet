from pathlib import Path

from environs import Env

from .settings import DbConfig, AppSettings, MongoConfig

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = Env()
env.read_env(path=BASE_DIR / ".env")

app_settings = AppSettings(
    db_conf=DbConfig(
        schema=env.str("DB_SCHEMA"), db_user=env.str("DB_USER"), db_passwd=env.str("DB_PASSWORD"),
        db_host=env.str("DB_HOST"), db_port=env.str("DB_PORT"), db_name=env.str("DB_NAME")
    ),
    # mongo_conf=MongoConfig(
    #     user=env.str("MONGO_USER"), password=env.str("MONGO_PASSWORD"),
    #     host=env.str("MONGO_HOST"), port=env.str("MONGO_PORT")
    # )
)
