"""Модуль настроек для работы приложения."""

from pathlib import Path

from envparse import env

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

if ENV_PATH.is_file():
    env.read_envfile(ENV_PATH)

POSTGRES_HOST = env.str("POSTGRES_HOST", default="localhost")
POSTGRES_PORT = env.str("POSTGRES_PORT", default=5432)
POSTGRES_USER = env.str("POSTGRES_USER", default="postgres")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", default="<PASSWORD>")
POSTGRES_DB = env.str("POSTGRES_DB", default="postgres")
