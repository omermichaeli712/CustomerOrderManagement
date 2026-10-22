
from Order import Order


class RegularOrder(Order):

    def calculate_total_price(self):
        total = 0

        for item in self.items:
            total += item.item_price

        return total
