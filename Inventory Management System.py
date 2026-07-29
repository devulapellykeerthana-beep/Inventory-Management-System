
inventory = []

# Add Product
def add_product():
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    product = {
        "ID": product_id,
        "Name": product_name,
        "Quantity": quantity,
        "Price": price
    }

    inventory.append(product)
    print("\nProduct Added Successfully!")

# View Stock Report
def stock_report():
    if len(inventory) == 0:
        print("\nNo Products Available!")
    else:
        print("\n========== STOCK REPORT ==========")
        for product in inventory:
            print("--------------------------------")
            print("Product ID :", product["ID"])
            print("Name       :", product["Name"])
            print("Quantity   :", product["Quantity"])
            print("Price      : Rs.", product["Price"])

# Search Product
def search_product():
    search = input("Enter Product Name: ")

    for product in inventory:
        if product["Name"].lower() == search.lower():
            print("\nProduct Found")
            print("ID       :", product["ID"])
            print("Name     :", product["Name"])
            print("Quantity :", product["Quantity"])
            print("Price    : Rs.", product["Price"])
            return

    print("Product Not Found!")

# Update Quantity
def update_quantity():
    search = input("Enter Product Name: ")

    for product in inventory:
        if product["Name"].lower() == search.lower():
            new_quantity = int(input("Enter New Quantity: "))
            product["Quantity"] = new_quantity
            print("Quantity Updated Successfully!")
            return

    print("Product Not Found!")

# Delete Product
def delete_product():
    search = input("Enter Product Name: ")

    for product in inventory:
        if product["Name"].lower() == search.lower():
            inventory.remove(product)
            print("Product Deleted Successfully!")
            return

    print("Product Not Found!")

# Main Menu
while True:

    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Quantity")
    print("4. Delete Product")
    print("5. Stock Report")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        search_product()

    elif choice == "3":
        update_quantity()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        stock_report()

    elif choice == "6":
        print("\nThank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")