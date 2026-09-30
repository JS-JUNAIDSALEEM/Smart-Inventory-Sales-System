# 🏪 Smart Inventory & Sales System

A command-line **Inventory and Sales Management System built with Python**.

This project allows users to manage products, update stock, process sales, apply discount coupons, track total earnings, and save shop data using JSON files.

The project was created to practice core Python concepts by building a practical shop management system.

---

## 🎯 Problem It Solves

Managing shop inventory manually can make it difficult to track stock, sales, and earnings.

This system provides a simple way to:

- Keep product records organized
- Track available stock
- Process customer sales
- Apply discount coupons
- Monitor total shop earnings
- Save inventory data for future use

---

## ✨ Features

- View current inventory
- Sell products and update stock automatically
- Apply discount coupons
- Track total earnings
- Restock existing products
- Add new products
- Delete products from inventory
- Save and load data using JSON
- Reset the shop database
- Handle common invalid user inputs using exception handling
- Prevent sales when available stock is insufficient

---

## 🛠️ Technologies Used

- **Python**
- **JSON** (Python's built-in `json` module)

### Python Concepts Used

- Object-Oriented Programming (OOP)
- Classes and objects
- Constructors and methods
- Dictionaries
- Loops and conditions
- File handling
- Exception handling
- User input validation

No external Python libraries are required.

---

## 📁 Project Structure

```text
Smart-Inventory-Sales-System/
│
├── main.py
├── README.md
├── .gitignore
├── shop_records.json          # Created/updated when data is saved
└── Screeshots/
    ├── Main Menu.png
    ├── Inventory.png
    ├── Successful Sale 1.0.png
    ├── Successful Sale 2.0.png
    └── Total Earning.png
```

### File Details

- **`main.py`** — Contains the main application logic.
- **`shop_records.json`** — Stores inventory and total earnings after saving. It is created automatically when you save and exit or reset the database; it may be absent before the first save.
- **`README.md`** — Contains project information and instructions.
- **`.gitignore`** — Excludes unnecessary local files from Git.
- **`Screeshots/`** — Contains screenshots of the command-line application.

---

## ⚙️ How to Run

### 1. Make sure Python 3 is installed

Check your Python version:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone https://github.com/JS-JUNAIDSALEEM/Smart-Inventory-Sales-System.git
```

*If your actual repository name differs, replace the URL above with its exact GitHub URL.*

### 3. Open the project folder

```bash
cd Smart-Inventory-Sales-System
```

### 4. Run the application

```bash
python main.py
```

No additional libraries need to be installed.

---

## 🖥️ Main Menu

When the program starts, the following menu is displayed:

```text
1. View Current Inventory
2. Sell Items to Customer
3. Check Total Earnings
4. Restock / Add New Item
5. Delete Item
6. Reset Database
7. Exit System
```

---

## 📦 Default Products

The system starts with the following products:

| Product | Price | Quantity |

|---|---:|---:|
| Chips | ₨20 | 20 |
| Juice | ₨50 | 10 |
| Biscuits | ₨40 | 5 |

These products can be restocked, deleted, or replaced with new products.

---

## 🎟️ Coupon Codes

The following coupon codes are available:

| Coupon | Discount |

|---|---:|

| `save10` | 10% |
| `welcome20` | 20% |

When a valid coupon is entered during a sale, the discount is automatically applied to the customer's bill.

---

## 💰 Sales and Earnings

When a product is sold:

- The system checks whether the product exists
- It verifies that enough stock is available
- The selected quantity is deducted from inventory
- A coupon can be applied
- The final bill amount is calculated
- The amount is added to total earnings

The user can check cumulative shop earnings from the main menu.

---

## 💾 Data Storage

The project uses **`shop_records.json`** to save:

- Product prices
- Product quantities
- Total earnings

When the program starts, previous shop data is loaded automatically if the file exists and contains valid JSON in the expected format.

When the user selects **Exit System**, the latest inventory and earnings data are saved. The database reset option also writes the restored default data to this file.

---

## ⚠️ Error Handling

The system handles several common invalid inputs and conditions, including:

- Invalid menu numbers
- Non-numeric quantity input
- Non-numeric product price input
- Products that do not exist
- Insufficient stock during sales
- Invalid coupon codes (sale continues without a discount)
- Missing JSON database file
- Invalid JSON syntax in the database file

**Note:** Some inputs, such as negative restock quantities or negative prices for new products, still need additional validation. This is a potential future improvement.

---

## 📸 Screenshots

Screenshots of the application are stored in the **`Screeshots/`** folder.

### Main Menu

![Main Menu](Screeshots/Main%20Menu.png)

### Inventory Report

![Inventory Report](Screeshots/Inventory.png)

### Successful Sale — Step 1

![Successful Sale 1](Screeshots/Successful%20Sale%201.0.png)

### Successful Sale — Step 2

![Successful Sale 2](Screeshots/Successful%20Sale%202.0.png)

### Total Earnings

![Total Earnings](Screeshots/Total%20Earning.png)

---

## 📚 What I Practiced

While building this project, I practiced:

- Classes and objects
- Constructors and methods
- Object-Oriented Programming
- Dictionaries
- Loops and conditions
- File handling
- JSON data storage
- Exception handling
- User input validation
- Product inventory management
- Sales processing
- Data persistence
- Problem solving

---

## 🚀 Future Improvements

As I continue improving my Python and AI skills, this project can be extended with:

- Graphical User Interface
- Sales history
- Product search
- Product categories
- Low-stock alerts
- Daily and monthly sales reports
- Data visualization
- SQLite or another database
- User authentication
- Stronger validation for prices and stock quantities

### Future AI Improvements

In future versions, the system could also include:

- Sales forecasting
- Product demand prediction
- Automatic restocking recommendations
- Best-selling product analysis

These features could turn the project into a more advanced AI-powered inventory system.

---

## 🎓 Project Purpose

This project is part of my learning journey toward becoming an **AI Engineer**.

The purpose of this project was to apply Python concepts in a practical application instead of only learning them theoretically.

---

## 👨‍💻 Author

### Junaid Saleem

Python Learner | Aspiring AI Engineer

- **GitHub:** [JS-JUNAIDSALEEM](https://github.com/JS-JUNAIDSALEEM)
- **LinkedIn:** [Junaid Saleem](https://www.linkedin.com/in/junaid-saleem-developer/)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
