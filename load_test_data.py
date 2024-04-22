"""Модуль для загрузки тестовых данных в бд."""

from models import (
    Base,
    Order,
    OrderProductLink,
    Product,
    Rack,
    RackProductLink,
    engine,
    session_maker,
)


def main():
    with session_maker() as session:
        Base.metadata.create_all(engine)
        session.add_all(
            [Rack(name="А"), Rack(name="Б"), Rack(name="Ж"), Rack(name="В"),
             Rack(name="З")],
        )
        session.add_all([
            Order(order_number=10, consumer_name="1"),
            Order(order_number=11, consumer_name="2"),
            Order(order_number=14, consumer_name="3"),
            Order(order_number=15, consumer_name="4"),
        ])
        session.add_all([
            Product(name="Ноутбук", article=1),
            Product(name="Телевизор", article=2),
            Product(name="Телефон", article=3),
            Product(name="Системный блок", article=4),
            Product(name="Часы", article=5),
            Product(name="Микрофон", article=6),
        ])
        session.add_all([
            RackProductLink(rack_id=1, product_id=1, main=True),
            RackProductLink(rack_id=1, product_id=2, main=True),
            RackProductLink(rack_id=1, product_id=5, main=False),
            RackProductLink(rack_id=2, product_id=3, main=True),
            RackProductLink(rack_id=5, product_id=3, main=False),
            RackProductLink(rack_id=4, product_id=3, main=False),
            RackProductLink(rack_id=3, product_id=4, main=True),
            RackProductLink(rack_id=3, product_id=5, main=True),
            RackProductLink(rack_id=3, product_id=6, main=True),
        ])
        session.add_all([
            OrderProductLink(order_id=1, product_id=1, count=2),
            OrderProductLink(order_id=2, product_id=2, count=3),
            OrderProductLink(order_id=3, product_id=1, count=3),
            OrderProductLink(order_id=1, product_id=3, count=1),
            OrderProductLink(order_id=3, product_id=4, count=4),
            OrderProductLink(order_id=4, product_id=5, count=1),
            OrderProductLink(order_id=1, product_id=6, count=1),
        ])
        session.commit()


if __name__ == "__main__":
    main()
