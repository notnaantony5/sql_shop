"""Модуль для удаления данных и таблиц из бд."""

from models import Base, engine, session_maker

with session_maker() as session:
    Base.metadata.drop_all(engine)
