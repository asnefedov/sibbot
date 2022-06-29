from dataclasses import dataclass
from environs import Env


@dataclass
class Bot:
    token: str


@dataclass
class Config:
    bot: Bot


def load_config():
    env = Env()
    env.read_env('.env')

    return Config(
        bot=Bot(
            token=env.str('BOT_TOKEN')
        )
    )
