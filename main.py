
from Customer import Customer
from CustomerType import CustomerType
from OrderItem import OrderItem
from PaymentType import PaymentType
from RegularOrder import RegularOrder
from VIPOrder import VIPOrder
from Gift import Gift


def main():
    # Create customers
    regular_customer = Customer(
        1, "John", "Doe",
        "john@example.com", "123 Street"
    )

    vip_customer = Customer(
        2, "Jane", "Doe",
        "jane@example.com", "456 Street",
        CustomerType.VIP, 0.05
    )

    # Create items
    book = OrderItem(1, "Book", 100)
    pen = OrderItem(2, "Pen", 20)
    notebook = OrderItem(3, "Notebook", 50)

    # Regular order
    regular_order = RegularOrder(
        1, "Regular Order", "123 Street",
        [book, pen],
        regular_customer,
        PaymentType.CASH
    )

    # VIP order
    vip_order = VIPOrder(
        2, "VIP Order", "456 Street",
        [book, notebook],
        vip_customer,
        PaymentType.CREDIT_CARD
    )

    print("Regular order total:", regular_order.total_price)
    print("VIP order total:", vip_order.total_price)

    # Favorite items
    print("VIP favorite items:")

    for item in vip_customer.favorite_items:
        print(item.item_name)

    vip_customer.remove_favorite_item(book)

    print("Favorites after removing Book:")

    for item in vip_customer.favorite_items:
        print(item.item_name)

    # Gift
    gift = Gift()
    vip_customer.take_gift(gift)
    vip_customer.open_gift()

    # Invalid VIP order
    try:
        invalid_order = VIPOrder(
            3, "Invalid VIP Order", "123 Street",
            [pen],
            regular_customer,
            PaymentType.CASH
        )

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

