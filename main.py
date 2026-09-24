# ==========================================
# 📊 SMART INVENTORY & SALES SYSTEM
# ==========================================

import json

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self):
        self.total_earnings = 0.0
        self.inventory = {
            "chips": Product("chips", 20.0, 20),
            "juice": Product("juice", 50.0, 10),
            "biscuits": Product("biscuits", 40.0, 5)
        }
        self.coupons = {"save10": 0.10, "welcome20": 0.20}

# ------------------------------------------
# DATA INITIAL LOADING
# ------------------------------------------

    def load_database(self):
        try:
            with open("shop_records.json", "r") as file:
                loaded_data = json.load(file)
                self.total_earnings = loaded_data["total_earnings"]

                # Raw text dictionary ko wapas Product Objects me convert karna
                self.inventory = {}
                for item_name, details in loaded_data["inventory"].items():
                    self.inventory[item_name] = Product(
                        item_name,
                        details["price"],
                        details["quantity"]
                    )

                print("📂 [System] Previous shop data loaded successfully!")

        except FileNotFoundError:
            print("✨ [System] No previous records found. Starting with fresh default stock!")

        except json.JSONDecodeError:
            print("⚠️ [System] Invalid database file. Starting with fresh default stock!")

# ------------------------------------------
# 1. SHOW INVENTORY
# ------------------------------------------

    def show_inventory(self):
        if len(self.inventory) == 0:
            print("\n⚠️ Notification: Shop inventory is completely empty!")
        else:
            print("\n" + "─"*50)
            print("       📋 CURRENT STOCK REPORT")
            print("─"*50)
            for item in self.inventory:
                price = self.inventory[item].price
                quantity = self.inventory[item].quantity
                print(f"🔹 {item.capitalize():<12} | Price: ₨ {price:<5.2f} | Stock: {quantity}")

# ------------------------------------------
# 2. SALE ITEM
# ------------------------------------------

    def sale_items(self):
        selected_item = input("\nEnter item name to sell: ").lower().strip()
        if selected_item == "0":
            print("🔙 Action cancelled. Going back to Main Menu...")
            return

        if selected_item in self.inventory:
            try:
                item_quantity = int(input(f"Enter quantity of {selected_item}: "))
            except ValueError:
                print("❌ Error: Invalid quantity entered!")
                return

            if item_quantity <= 0:
                print("❌ Error: Quantity must be greater than zero!")
            elif item_quantity > self.inventory[selected_item].quantity:
                print(f"❌ Transaction Failed: Not enough stock! Available: {self.inventory[selected_item].quantity}")
            else:
                self.inventory[selected_item].quantity -= item_quantity
                price_item = self.inventory[selected_item].price * item_quantity

                coupon_code = input("🎟️ Enter coupon code (or press Enter to skip): ").lower().strip()
                if coupon_code == "":
                    print("ℹ️ No coupon entered. Original price applied.")
                elif coupon_code in self.coupons:
                    discount_rate = self.coupons[coupon_code]
                    discount_amount = price_item * discount_rate
                    price_item -= discount_amount
                    print(f"✅ Success: Coupon '{coupon_code.upper()}' applied! You saved ₨ {discount_amount:.2f}")
                else:
                    print("❌ Invalid Coupon Code! No discount applied.")

                self.total_earnings += price_item
                print(f"\n✅ Success: Sold {item_quantity} {selected_item.capitalize()}!")
                print(f"💵 Bill Amount: ₨ {price_item:.2f}")
        else:
            print("❌ Error: This item does not exist in the inventory!")

# ------------------------------------------
# 3. SHOW TOTAL EARNINGS
# ------------------------------------------

    def show_total_earnings(self):
        print("\n" + "─"*30)
        if self.total_earnings == 0:
            print("💸 Financial Statement: No earnings recorded yet.")
        else:
            print(f"💰 Cumulative Revenue: ₨ {self.total_earnings:.2f}")
        print("─"*30)

# ------------------------------------------
# 4. RESTOCK OR ADD ITEM
# ------------------------------------------

    def restock_or_add_item(self):
        new_stock = input("\nEnter item name to restock/add: ").lower().strip()
        if new_stock == "0" or new_stock == "":
            print("🔙 Action cancelled. Going back to Main Menu...")
            return

        if new_stock in self.inventory:
            try:
                add_quantity = int(input(f"Enter additional quantity for {new_stock}: "))
            except ValueError:
                print("❌ Error: Invalid quantity number!")
                return

            self.inventory[new_stock].quantity += add_quantity
            print(f"✅ Restock Complete: {new_stock.capitalize()} total stock is now {self.inventory[new_stock].quantity}.")
        else:
            print(f"\n✨ System Alert: '{new_stock.capitalize()}' is a new product.")
            try:
                new_item_price = float(input(f"Set base price for {new_stock}: ₨ "))
                new_item_quantity = int(input("Enter initial stock quantity: "))
            except ValueError:
                print("❌ Error: Invalid numerical fields entered!")
                return

            self.inventory[new_stock] = Product(new_stock, new_item_price, new_item_quantity)
            print(f"🎉 Database Updated: {new_stock.capitalize()} successfully added!")

# ------------------------------------------
#  5. DELETE ITEM
# ------------------------------------------

    def delete_item(self):
        item_to_delete = input("\nEnter item name to DELETE from inventory (or '0'/Enter to cancel): ").lower().strip()
        if item_to_delete == "" or item_to_delete == "0":
            print("🔙 Action cancelled. Going back to Main Menu...")
            return

        if item_to_delete in self.inventory:
            del self.inventory[item_to_delete]
            print(f"🗑️ Success: {item_to_delete.capitalize()} has been removed from the inventory records!")
        else:
            print("❌ Error: Item not found in the inventory.")

# ------------------------------------------
# 6. RESET DATABASE
# ------------------------------------------

    def reset_database(self):
        confirm = input("\n⚠️ WARNING: Are you sure you want to reset all records? (yes/no): ").lower().strip()
        if confirm == "yes":
            self.inventory = {
                "chips": Product("chips", 20.0, 20),
                "juice": Product("juice", 50.0, 10),
                "biscuits": Product("biscuits", 40.0, 5)
            }
            self.total_earnings = 0.0

            serializable_inventory = {}
            for item_name, obj in self.inventory.items():
                serializable_inventory[item_name] = {"price": obj.price, "quantity": obj.quantity}

            data_to_save = {
                "inventory": serializable_inventory,
                "total_earnings": self.total_earnings
            }

            with open("shop_records.json", "w") as file:
                json.dump(data_to_save, file)

            print("🔄 Success: Database reset! Default stock restored.")
        else:
            print("🔙 Reset cancelled. Your data is safe.")

# ------------------------------------------
# 7. SAVE AND EXIT
# ------------------------------------------

    def save_and_exit(self):
    # Serializing into standard dictionary text format for OBJECTS
        serializable_inventory = {}
        for item_name, obj in self.inventory.items():
            serializable_inventory[item_name] = {"price": obj.price, "quantity": obj.quantity}

        data_to_save = {
            "inventory": serializable_inventory,
            "total_earnings": self.total_earnings
        }
        with open("shop_records.json", "w") as file:
            json.dump(data_to_save, file)
        print("\n💾 Data saved successfully!")
        print("\n👋 System Shutdown. Thank you for using Digital Shop Manager!\n")

# ------------------------------------------
# MAIN SYSTEM LOOP
# ------------------------------------------

# Instantiating the main object
my_shop = Shop()
my_shop.load_database()

while True:
    print("\n" + "═"*35)
    print("     🏪 DIGITAL SHOP MENU       ")
    print("═"*35)
    print("  1. 📋 View Current Inventory")
    print("  2. 🛒 Sell Items to Customer")
    print("  3. 💰 Check Total Earnings")
    print("  4. 📦 Restock / Add New Item")
    print("  5. 🗑️  Delete Item")
    print("  6. 🔄 Reset Database")
    print("  7. 🚪 Exit System")
    print("─"*35)

    try:
        choice = int(input("👉 Enter your choice (1-7): ")) 
    except ValueError:
        print("\n❌ Error: Please enter a valid menu number!")
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
        my_shop.save_and_exit()
        break
    else:
        print("\n❌ Error: Out of bounds choice! Please select between 1 and 7.")
