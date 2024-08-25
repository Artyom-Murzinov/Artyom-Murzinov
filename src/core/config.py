from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    send_report_to_owner: bool


@dataclass
class Database:
    host: str
    user: str
    name: str
    port: str
    password: str


@dataclass
class Config:
    tg_bot: TgBot
    db: Database


def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            send_report_to_owner=env.bool("SEND_REPORT_TO_OWNER"),
        ),
        db=Database(
            host=env.str("POSTGRES_HOST"),
            user=env.str("POSTGRES_USER"),
            name=env.str("POSTGRES_DB"),
            port=env.str("POSTGRES_PORT"),
            password=env.str("POSTGRES_PASSWORD"),
        ),
    )
