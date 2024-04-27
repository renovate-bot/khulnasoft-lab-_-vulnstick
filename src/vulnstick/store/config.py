from dataclasses import dataclass

DEFAULT_STORE_ROOT = ".vulnstick"


@dataclass
class StoreConfig:
    store_root: str = DEFAULT_STORE_ROOT


_config = StoreConfig()


def get() -> StoreConfig:
    return _config


def set_values(**kwargs):
    for k, v in kwargs.items():
        setattr(get(), k, v)
