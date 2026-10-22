
from abc import ABC, abstractmethod
from datetime import datetime
from Customer import Customer
from OrderItem import OrderItem


class Order(ABC):

    used_ids = []

    def __init__(self, order_id, name, delivery_address,
                 items, customer, payment_type, order_date=None):

        if order_id in Order.used_ids:
            raise ValueError("Order ID already exists")

        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer")

        item_ids = []

        for item in items:
            if not isinstance(item, OrderItem):
                raise ValueError("Invalid order item")

            if item.item_id in item_ids:
                raise ValueError("Duplicate item ID in order")

            item_ids.append(item.item_id)

        self.order_id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = list(items)
        self.customer = customer
        self.payment_type = payment_type

        if order_date is None:
            self.order_date = datetime.now()
        else:
            self.order_date = order_date

        self.validate_order()
        self.total_price = self.calculate_total_price()

        Order.used_ids.append(order_id)

        for item in self.items:
            self.customer.add_favorite_item(item)

    def validate_order(self):
        pass

    @abstractmethod
    def calculate_total_price(self):
        pass
