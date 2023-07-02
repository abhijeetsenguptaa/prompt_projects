from tabulate import tabulate

zomatoInventory = []
zomatoOrders = []

# File paths
INVENTORY_FILE = 'inventory.txt'
ORDERS_FILE = 'orders.txt'

# Save inventory data to file
def save_inventory():
    with open(INVENTORY_FILE, 'w') as file:
        headers = ["ID", "Name", "Price", "Availability"]
        data = [[item["id"], item["name"], item["price"], item["availability"]] for item in zomatoInventory]
        table = tabulate(data, headers, tablefmt="grid")
        file.write(table)


# Save orders data to file
def save_orders():
    with open(ORDERS_FILE, 'w') as file:
        headers = ["ID", "Name", "Item Name", "Quantity", "Status", "Price"]
        data = [[item["id"], item["name"], item["item_name"], item["quantity"], item["status"], item["price"]] for item in zomatoOrders]
        table = tabulate(data, headers, tablefmt="grid")
        file.write(table)


# Adding Inventory
def addItem(name, price, availability):
    id = len(zomatoInventory) + 1
    item = {"id": id, "name": name, "price": price, "availability": availability}
    zomatoInventory.append(item)
    print("Item added to the Inventory..")
    save_inventory()


# Removing an Item
def removeItem(id):
    for item in zomatoInventory:
        if item["id"] == id:
            zomatoInventory.remove(item)
            print(f"Item with ID:{id} has been removed.")
            save_inventory()
            break
    else:
        print(f"Item with ID:{id} not available")


# Updating the Availability
def updateItem(id, availability):
    for item in zomatoInventory:
        if item["id"] == id:
            item["availability"] = availability
            print(f"Item with ID:{id} has been updated.")
            save_inventory()
            break
    else:
        print(f"Item with ID:{id} not available.")


# Display the Inventory
def displayItem():
    if not zomatoInventory:
        print("Inventory is Empty")
    else:
        headers = ["ID", "Name", "Price", "Availability"]
        data = [[item["id"], item["name"], item["price"], item["availability"]] for item in zomatoInventory]
        print(tabulate(data, headers, tablefmt="grid"))


# Adding Order
def addingOrder(name, item_name, quantity, status, price):
    id = len(zomatoOrders) + 1
    order = {
        "id": id,
        "name": name,
        "item_name": item_name,
        "quantity": quantity,
        "status": status,
        "price": price
    }
    zomatoOrders.append(order)
    print("Your order has been successfully placed..")
    save_orders()


# Updating the order status
def updateOrderStatus(id, status):
    for item in zomatoOrders:
        if item["id"] == id:
            item["status"] = status
            print("Order status has been updated..")
            save_orders()
            break
    else:
        print("Order can't be found..")


# Review all the Orders
def reviewOrders():
    if not zomatoOrders:
        print("No Orders till now.")
    else:
        headers = ["ID", "Name", "Item Name", "Quantity", "Status", "Price"]
        data = [[item["id"], item["name"], item["item_name"], item["quantity"], item["status"], item["price"]] for item in zomatoOrders]
        print(tabulate(data, headers, tablefmt="grid"))


while True:
    print("\nWelcome to Zomato Chronicles: The Great Food Fiasco")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Update item availability")
    print("4. Display item inventory")
    print("5. Add a new order")
    print("6. Update the status")
    print("7. Review all orders")
    print("8. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        availability = input("Is the item available? (yes/no): ")
        addItem(name, price, availability)

    elif choice == "2":
        id = int(input("Enter item ID to remove: "))
        removeItem(id)

    elif choice == "3":
        id = int(input("Enter item ID to update: "))
        availability = input("Update item availability (yes/no): ")
        updateItem(id, availability)

    elif choice == "4":
        displayItem()

    elif choice == "5":
        name = input("Enter the customer's name: ")
        item_name = input("Enter the item you want to purchase: ")
        quantity = int(input("Enter the quantity: "))
        total_price = 0
        for item in zomatoInventory:
            if item["name"] == item_name:
                total_price = item["price"] * quantity
                break
        status = input("Enter the status of the order (received/preparing/ready for pickup/delivered): ")
        addingOrder(name, item_name, quantity, status, total_price)

    elif choice == "6":
        id = int(input("Enter the order ID to update: "))
        status = input("Update the status (received/preparing/ready for pickup/delivered): ")
        updateOrderStatus(id, status)

    elif choice == "7":
        reviewOrders()

    elif choice == "8":
        print("Thanks for using Zomato Chronicles")
        save_inventory()
        save_orders()
        break
