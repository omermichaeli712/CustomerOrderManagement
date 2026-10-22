
class OrderItem:

    def __init__(self, item_id, item_name, item_price):
        if item_price < 0:
            raise ValueError("Item price cannot be negative")

        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price

    def __str__(self):
        return f"{self.item_name} - {self.item_price}"
