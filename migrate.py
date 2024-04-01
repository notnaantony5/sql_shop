"""Скрипт для миграциии таблиц в актульную базу данных."""

from database import Database
from settings import settings

db = Database(settings=settings)
