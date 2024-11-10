# bill.py

from order import ordered_items


def generate_bill():
    if not ordered_items:
        print("No items ordered yet!")
        return

    print("\nYour Bill:")
    total_amount = 0
    for item in ordered_items.values():
        item_total = item['price'] * item['quantity']
        total_amount += item_total
        print(f"{item['name']} x {item['quantity']} = ₹{item_total}")

    print(f"Total Amount: ₹{total_amount}")
