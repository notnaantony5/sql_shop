"""Модуль c описанием моделей БД для работы приложения."""

from sqlalchemy import ForeignKey, PrimaryKeyConstraint, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)

from settings import (
    POSTGRES_DB,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
)

engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")

session_maker = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    __abstract__ = True


class Rack(Base):
    __tablename__ = "rack"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(index=True, unique=True)

    racks_product_links: Mapped[list["RackProductLink"]] = relationship(
        "RackProductLink", back_populates="rack")


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_number: Mapped[int] = mapped_column(index=True, unique=True)
    consumer_name: Mapped[str]

    orders_product_links: Mapped[list["OrderProductLink"]] = relationship(
        "OrderProductLink", back_populates="order")


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(index=True)
    article: Mapped[int] = mapped_column(index=True, unique=True)

    orders_product_links: Mapped[list["OrderProductLink"]] = relationship(
        "OrderProductLink", back_populates="product")

    racks_product_links: Mapped[list["RackProductLink"]] = relationship(
        "RackProductLink", back_populates="product")


class OrderProductLink(Base):
    __tablename__ = "order_product_link"
    __table_args__ = (PrimaryKeyConstraint("order_id", "product_id"),)

    count: Mapped[int]

    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    order: Mapped["Order"] = relationship("Order",
                                          back_populates="orders_product_links")
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped["Product"] = relationship("Product",
                                              back_populates="orders_product_links")


class RackProductLink(Base):
    __tablename__ = "rack_product_link"
    __table_args__ = (PrimaryKeyConstraint("rack_id", "product_id"),)

    main: Mapped[bool]

    rack_id: Mapped[int] = mapped_column(ForeignKey("rack.id"))
    rack: Mapped["Rack"] = relationship("Rack",
                                        back_populates="racks_product_links")

    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped["Product"] = relationship("Product",
                                              back_populates="racks_product_links")
