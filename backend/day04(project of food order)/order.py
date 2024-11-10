# order.py

from display import items,display_items

# This dictionary will hold the order details
ordered_items = {}


def order_item():

    item_num = int(input("Enter the item number to order: "))

    if item_num in items:
        quantity = int(input(f"How many {items[item_num]['name']} would you like to order? "))
        if item_num in ordered_items:
            ordered_items[item_num]['quantity'] += quantity
        else:
            ordered_items[item_num] = {
                "name": items[item_num]["name"],
                "price": items[item_num]["price"],
                "quantity": quantity
            }
        print(f"{quantity} {items[item_num]['name']}(s) added to your order.")
    else:
        print("Invalid item number. Please try again.")
