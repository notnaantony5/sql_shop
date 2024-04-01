"""Модуль настроек для работы приложения."""

from pathlib import Path

from envparse import env

from database import DatabaseSettings

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

if ENV_PATH.is_file():
    env.read_envfile(ENV_PATH)

settings = DatabaseSettings(
    host=env.str("DB_HOST", ""),
    port=env.int("DB_PORT", 0),
    db=env.str("DB_NAME", ""),
    user=env.str("DB_USER", ""),
    password=env.str("DB_PASSWORD", ""),
)
