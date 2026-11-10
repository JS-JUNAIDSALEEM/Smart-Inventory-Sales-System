# Smart Inventory & Sales System

## Project Overview

This project is a Python-based shop management system. It helps manage products, sell items, update stock, and keep records of shop earnings.

I created this project to practice Python programming, Object-Oriented Programming (OOP), and file handling using JSON.

## Features

- View current product inventory.
- Sell products to customers.
- Apply discount coupons.
- Check total shop earnings.
- Restock existing products.
- Add new products.
- Delete products from inventory.
- Reset shop records.
- Save and load data using a JSON file.
- Handle invalid user inputs.

## Technologies Used

- Python
- JSON
- Object-Oriented Programming (OOP)

## Project Structure

```text
Smart-Inventory-Sales-System/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── tests/
    └── test_shop.py
```

## How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/JS-JUNAIDSALEEM/Smart-Inventory-Sales-System.git
```

**2. Open the project folder**

```bash
cd Smart-Inventory-Sales-System
```

**3. Run the application**

```bash
python main.py
```

## Testing

A separate `test_shop.py` file is included to check basic project features.

It contains 10 simple checks for:

- Default inventory.
- Default product stock.
- Total shop earnings.
- Coupon codes.
- Second coupon code.
- Product objects.
- Product prices.
- Database version.
- Number of default products.
- Initial inventory quantity.

Run the tests using:

```bash
py -m tests.test_shop
```

**Note:** These are basic print-based checks. They display whether each check passes or fails.

## Data Storage

The project uses a JSON file to store shop records.

The file is named `shop_records.json` and is located inside a local `data/` folder when used by the application.

This file works as a local working data file. It helps the application save and load shop records between program runs.

The file stores:

- **Inventory:** Product names, prices, and available stock quantities.
- **Total Earnings:** Total money earned from successful sales after discounts.
- **Database Version:** The current database structure version. It helps the program manage changes in the database format.

**Note:** The `shop_records.json` file is excluded from the GitHub repository using `.gitignore`. It is a local data file used by the application, not a permanent project source file. Its contents can change when products are sold, restocked, added, or deleted.

## What I Learned

While working on this project, I practiced:

- Creating classes and objects in Python.
- Working with dictionaries.
- Using loops and conditional statements.
- Handling user input and errors.
- Reading and writing JSON files.
- Organizing a Python project.
- Writing basic tests.

## Future Improvements

- Add a graphical user interface.
- Generate sales reports.
- Add customer records.
- Improve transaction history.
- Save records automatically after successful operations.
- Add more testing features.

## 👨‍💻 Author

### Junaid Saleem

- **GitHub:** [JS-JUNAIDSALEEM](https://github.com/JS-JUNAIDSALEEM)
- **LinkedIn:** [Junaid Saleem](https://www.linkedin.com/in/junaid-saleem-developer/)
