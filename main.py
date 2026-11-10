
import json
import os

# PRODUCT CLASS

class Product:

    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity

    def show_details(self):

        print("\nProduct Details")
        print("-------------------------")
        print(f"Product Name: {self.name.capitalize()}")
        print(f"Price: Rs. {self.price:.2f}")
        print(f"Available Stock: {self.quantity}")


# SHOP CLASS

class Shop:

    def __init__(self):
        self.total_earnings = 0.0

        self.inventory = {
            "chips": Product("chips", 20.0, 20),
            "juice": Product("juice", 50.0, 10),
            "biscuits": Product("biscuits", 40.0, 5),
            "chocolate": Product("chocolate", 80.0, 15),
            "soda": Product("soda", 60.0, 12),
            "water": Product("water", 30.0, 25),
            "candy": Product("candy", 10.0, 50),
            "noodles": Product("noodles", 50.0, 18)
        }

        self.coupons = {
            "save10": 0.10,
            "welcome20": 0.20
        }

        self.database_version = 2

# 1. SHOW INVENTORY

    def show_inventory(self):

        if len(self.inventory) == 0:
            print("\nShop inventory is empty.")

        else:
            print("\n" + "─" * 50)
            print("        CURRENT STOCK REPORT")
            print("─" * 50)

            for item in self.inventory:
                price = self.inventory[item].price
                quantity = self.inventory[item].quantity

                print(f"{item.capitalize():<12} | Price: Rs. {price:<5.2f} | Stock: {quantity}")

# 2. SALE ITEM

    def sale_items(self):

        selected_item = input("\nEnter item name to sell: ").lower().strip()

        if selected_item == "0":
            print("Action cancelled.")
            return

        if selected_item not in self.inventory:
            print("Error: This item does not exist in inventory!")
            return

        try:
            item_quantity = int(input(f"Enter quantity of {selected_item}: "))

        except ValueError:
            print("Error: Invalid quantity entered!")
            return

        if item_quantity <= 0:
            print("Error: Quantity must be greater than zero!")
            return

        if item_quantity > self.inventory[selected_item].quantity:
            print(f"Transaction Failed: Not enough stock! Available: {self.inventory[selected_item].quantity}")
            return

        price_item = self.inventory[selected_item].price * item_quantity
        coupon_code = input("Enter coupon code (save10 or welcome20): ").lower().strip()

        if coupon_code == "" or coupon_code == "0":
            print("No coupon entered. Original price applied.")

        elif coupon_code in self.coupons:

            discount_rate = self.coupons[coupon_code]
            discount_amount = price_item * discount_rate
            price_item -= discount_amount

            print(f"Coupon applied! You saved Rs. {discount_amount:.2f}")

        else:
            print("Invalid Coupon Code! No discount applied.")

        self.inventory[selected_item].quantity -= item_quantity
        self.total_earnings += price_item

        print(f"\nSuccess: Sold {item_quantity} {selected_item.capitalize()}!")
        print(f"Bill Amount: Rs. {price_item:.2f}")

        # Save database after successful sale
        self.save_database()

# 3. SHOW TOTAL EARNINGS

    def show_total_earnings(self):

        print("\n" + "─" * 30)

        if self.total_earnings == 0:
            print("Financial Statement: No earnings recorded yet.")

        else:
            print(f"Total Revenue: Rs. {self.total_earnings:.2f}")

        print("─" * 30)

# 4. RESTOCK OR ADD ITEM

    def restock_or_add_item(self):

        new_stock = input("\nEnter item name to restock/add: ").lower().strip()

        if new_stock == "0" or new_stock == "":
            print("Action cancelled.")
            return

        if new_stock in self.inventory:
            try:
                add_quantity = int(input(f"Enter additional quantity for {new_stock}: "))

            except ValueError:
                print("Error: Invalid quantity number!")
                return

            if add_quantity <= 0:
                print("Error: Quantity must be greater than zero!")
                return

            self.inventory[new_stock].quantity += add_quantity

            print(f"Restock Complete: {new_stock.capitalize()} total stock is now {self.inventory[new_stock].quantity}.")

            # Save database after successful restock
            self.save_database()

        else:
            print(f"\n'{new_stock.capitalize()}' is a new product.")

            try:
                new_item_price = float(input(f"Set base price for {new_stock}: Rs. "))
                new_item_quantity = int(input("Enter initial stock quantity: "))

            except ValueError:
                print("Error: Invalid numerical fields entered!")
                return

            if new_item_price <= 0 or new_item_quantity <= 0:
                print("Error: Price and quantity must be greater than zero!")
                return

            self.inventory[new_stock] = Product(
                new_stock,
                new_item_price,
                new_item_quantity
            )

            print(f"{new_stock.capitalize()} successfully added!")

            # Save database after adding new product
            self.save_database()

# 5. DELETE ITEM

    def delete_item(self):

        item_to_delete = input("\nEnter item name to DELETE (or 0 to cancel): ").lower().strip()

        if item_to_delete == "" or item_to_delete == "0":
            print("Action cancelled.")
            return

        if item_to_delete in self.inventory:
            del self.inventory[item_to_delete]
            print(f"{item_to_delete.capitalize()} has been removed from inventory!")

            # Save database after successful deletion
            self.save_database()

        else:
            print("Error: Item not found in inventory.")

# 6. RESET DATABASE

    def reset_database(self):

        confirm = input("\nAre you sure you want to reset all records? (yes/no): ").lower().strip()

        if confirm == "yes":
            self.inventory = {
                "chips": Product("chips", 20.0, 20),
                "juice": Product("juice", 50.0, 10),
                "biscuits": Product("biscuits", 40.0, 5),
                "chocolate": Product("chocolate", 80.0, 15),
                "soda": Product("soda", 60.0, 12),
                "water": Product("water", 30.0, 25),
                "candy": Product("candy", 10.0, 50),
                "noodles": Product("noodles", 50.0, 18)
            }

            self.total_earnings = 0.0

            print("Database reset! Default stock restored.")
            self.save_database()

        else:
            print("Reset cancelled. Your data is safe.")

# 7. SAVE DATABASE

    def save_database(self):

        serializable_inventory = {}

        for item_name, obj in self.inventory.items():
            serializable_inventory[item_name] = {
                "price": obj.price,
                "quantity": obj.quantity
            }

        data_to_save = {
            "inventory": serializable_inventory,
            "total_earnings": self.total_earnings,
            "database_version": self.database_version
        }

        try:
            os.makedirs("data", exist_ok=True)

            with open("data/shop_records.json", "w") as file:
                json.dump(data_to_save, file, indent=4)

            print("\nData saved successfully!")

        except OSError as error:
            print(f"Error saving database: {error}")

# 8. LOAD DATABASE

    def load_database(self):

        if not os.path.exists("data/shop_records.json"):
            print("No previous records found. Starting with fresh default stock!")
            return

        try:
            with open("data/shop_records.json", "r") as file:
                loaded_data = json.load(file)

            inventory_data = loaded_data["inventory"]
            total_earnings = float(loaded_data["total_earnings"])

            if total_earnings < 0:
                raise ValueError("Invalid total earnings.")

            new_inventory = {}

            for item_name, details in inventory_data.items():
                price = float(details["price"])
                quantity = int(details["quantity"])

                if price <= 0 or quantity < 0:
                    raise ValueError("Invalid product price or quantity.")

                new_inventory[item_name] = Product(
                    item_name,
                    price,
                    quantity
                )

            old_version = loaded_data.get("database_version", 1)

    # Add missing products from updated inventory

            if old_version < self.database_version:

                new_products = {
                    "chocolate": Product("chocolate", 80.0, 15),
                    "soda": Product("soda", 60.0, 12),
                    "water": Product("water", 30.0, 25),
                    "candy": Product("candy", 10.0, 50),
                    "noodles": Product("noodles", 50.0, 18)
                }

                for item_name, product in new_products.items():

                    if item_name not in new_inventory:
                        new_inventory[item_name] = product

                print("Inventory updated with new products!")

            self.inventory = new_inventory
            self.total_earnings = total_earnings

            print("Previous shop data loaded successfully!")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError, OSError) as error:
            print(f"Invalid database file. Starting with fresh default stock! ({error})")


# MAIN SYSTEM LOOP

# Creating the main shop object

if __name__ == "__main__":

    my_shop = Shop()
    my_shop.load_database()

    while True:

        print("\n" + "═" * 40)
        print("       SMART INVENTORY & SALES SYSTEM")
        print("═" * 40)

        print("  1. View Current Inventory")
        print("  2. Sell Items to Customer")
        print("  3. Check Total Earnings")
        print("  4. Restock / Add New Item")
        print("  5. Delete Item")
        print("  6. Reset Database")
        print("  7. Save and Exit")

        print("─" * 40)

        try:
            choice = int(input("Enter your choice (1-7): "))

        except ValueError:
            print("\nError: Please enter a valid menu number!")
            continue

        if choice == 1:
            my_shop.show_inventory()

        elif choice == 2:
            my_shop.sale_items()

        elif choice == 3:
            my_shop.show_total_earnings()

        elif choice == 4:
            my_shop.restock_or_add_item()

        elif choice == 5:
            my_shop.delete_item()

        elif choice == 6:
            my_shop.reset_database()

        elif choice == 7:
            my_shop.save_database()

            print("\nSystem Shutdown.")
            print("Thank you for using Smart Inventory & Sales System!")

            break

        else:
            print("\nError: Please select a number between 1 and 7.")
