
from Order import Order
from CustomerType import CustomerType


class VIPOrder(Order):

    def validate_order(self):
        if self.customer.customer_type != CustomerType.VIP:
            raise ValueError(
                "VIP order is allowed only for VIP customers"
            )

    def calculate_total_price(self):
        total = 0

        for item in self.items:
            total += item.item_price

        discount = self.customer.customer_discount

        if discount is None:
            discount = 0

        total = total * (1 - discount)

        return total
