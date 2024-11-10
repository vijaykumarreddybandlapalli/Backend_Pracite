

import display
import order
import bill

def menu():
    while True:
        print("\n1. Display Items")
        print("2. Order Your Item")
        print("3. Generate Bill")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display.display_items()
        elif choice == 2:
            order.order_item()
        elif choice == 3:
            bill.generate_bill()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
