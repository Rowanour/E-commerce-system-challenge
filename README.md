# Fawry Rise Journey  
**Full Stack Development Internship Challenge**

This is a Python implementation of the Fawry e-commerce system challenge. The goal is to simulate an online shopping experience with product handling, cart management, checkout processing, and shipping logic.

---

## What It Does

- **Product Definition**  
  Products have a name, price, quantity, Expiry date (e.g., Cheese, Biscuits) and Weight (if shipping is needed, like TVs or Cheese)

- **Cart Management**  
  Customers can:
  - Add items to a cart (without exceeding stock)
  - See errors if products are expired or out of stock

- **Checkout Logic**  
  On checkout:
  - Calculates subtotal and shipping fees
  - Deducts from customer balance
  - Prints a detailed receipt
  - Validates empty cart, stock, expiry, and balance

- **Shipping**  
  Collects items that require shipping and prints a shipment summary (name, quantity, total weight).

---

## Tech Used

- Python 3
- OOP principles (inheritance, abstraction via `abc`)
- `datetime` for expiry checks