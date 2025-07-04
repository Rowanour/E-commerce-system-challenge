from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Product:
    def __init__(self, name, price, quantity, expiry_date=None, weight=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expiry_date = expiry_date
        self.weight = weight

    def is_expired(self):
        return self.expiry_date is not None and self.expiry_date < datetime.now()

    def is_shippable(self):
        return self.weight is not None


class Shippable(ABC):
    @abstractmethod
    def getName(self): pass

    @abstractmethod
    def getWeight(self): pass


class ShippableProduct(Product, Shippable):
    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product, quantity):
        if quantity > product.quantity:
            raise ValueError("Requested quantity exceeds stock.")
        self.items.append(CartItem(product, quantity))

    def is_empty(self):
        return len(self.items) == 0

    def get_shippables(self):
        return [item.product for item in self.items if item.product.is_shippable()]

    def calculate_subtotal(self):
        return sum(item.product.price * item.quantity for item in self.items)

    def calculate_shipping(self):
        return sum(item.product.weight * 10 for item in self.items if item.product.is_shippable())


class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class ShippingService:
    @staticmethod
    def ship(items):
        print("** Shipment notice **")
        total_weight = 0
        for item in items:
            weight = item.weight
            count = sum(i.quantity for i in cart.items if i.product.name == item.name)
            total_weight += weight * count
            print(f"{count}x {item.name}\t{int(weight * 1000)}g")
        print(f"Total package weight {round(total_weight, 1)}kg\n")


def checkout(customer, cart):
    if cart.is_empty():
        raise ValueError("Cart is empty.")

    for item in cart.items:
        if item.product.is_expired():
            raise ValueError(f"{item.product.name} is expired.")
        if item.quantity > item.product.quantity:
            raise ValueError(f"{item.product.name} is out of stock.")

    subtotal = cart.calculate_subtotal()
    shipping = cart.calculate_shipping()
    total = subtotal + shipping

    if customer.balance < total:
        raise ValueError("Insufficient balance.")

    for item in cart.items:
        item.product.quantity -= item.quantity

    customer.balance -= total

    shippables = cart.get_shippables()
    if shippables:
        ShippingService.ship(shippables)

    print("** Checkout receipt **")
    for item in cart.items:
        print(f"{item.quantity}x {item.product.name}\t{item.product.price * item.quantity}")
    print("----------------------")
    print(f"Subtotal\t{subtotal}")
    print(f"Shipping\t{int(shipping)}")
    print(f"Amount\t\t{int(total)}")
    print(f"Balance left\t{int(customer.balance)}\n")



cheese = ShippableProduct("Cheese", 100, 5, datetime.now() + timedelta(days=1), 0.2)
biscuits = ShippableProduct("Biscuits", 150, 2, datetime.now() + timedelta(days=1), 0.7)
tv = ShippableProduct("TV", 3000, 2, None, 8.0)
scratch_card = Product("Scratch Card", 50, 10) 

customer = Customer("John", 1000)
cart = Cart()
cart.add(cheese, 2)
cart.add(biscuits, 1)
cart.add(scratch_card, 1)

checkout(customer, cart)