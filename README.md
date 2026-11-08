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
├── data/
│   └── shop_records.json
│
└── tests/
    └── test_shop.py
```

## How to Run the Project

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
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

It includes simple tests for:

- Default inventory
- Product stock
- Product prices
- Coupon codes
- Total earnings
- Database version

Run the tests using:

```bash
python -m tests.test_shop
```

## Data Storage

The project uses a JSON file to save shop records.

Product information, stock quantities, and total earnings are saved in:

`data/shop_records.json`

This allows the shop data to be loaded again when the application starts.

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
- Add more testing features.

## 👨‍💻 Author

### Junaid Saleem

- **GitHub:** [JS-JUNAIDSALEEM](https://github.com/JS-JUNAIDSALEEM)
- **LinkedIn:** [Junaid Saleem](https://www.linkedin.com/in/junaid-saleem-developer/)
- 
