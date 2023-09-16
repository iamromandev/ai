from enum import Enum

from functools import cached_property, lru_cache

from pydantic import BaseSettings


class Env(str, Enum):
    local = "local"
    dev = "dev"
    stage = "stage"
    prod = "prod"


class Config(BaseSettings):
    env: Env
    debug: bool

    cache_host: str
    cache_port: int

    db_root_password: str
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    @cached_property
    def cache_url(self) -> str:
        return f"redis://{self.cache_host}:{self.cache_port}/0"

    @cached_property
    def db_url(self) -> str:
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        keep_untouched = (cached_property,)
        env_file = ".env"
        use_enum_values = True


@lru_cache
def get_config() -> Config:
    return Config()
