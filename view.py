"""tewtw."""
from sqlalchemy.orm import joinedload

from models import (
    Order,
    OrderProductLink,
    Product,
    Rack,
    RackProductLink,
    session_maker,
)


class View:
    """dfdfsg."""

    def __init__(self: "View", order_numbers: list[int]) -> None:
        """_summary_.

        Args:
        ----
            self (View): _description_.
            order_numbers (list[int]): _description_.

        """
        n = "\n"
        self.order_numbers = order_numbers
        with session_maker() as session:
            racks = session.query(Rack).filter(
                Order.order_number.in_([10])).options(
                joinedload(Rack.racks_product_links).subqueryload(
                    RackProductLink.product).subqueryload(
                    Product.orders_product_links).subqueryload(
                    OrderProductLink.order)).all()
            for rack in racks:
                print(rack.name)
