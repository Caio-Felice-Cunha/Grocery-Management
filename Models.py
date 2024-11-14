from datetime import datetime


class Category:
    def __init__(self, category):
        self.category = category


class Products:
    def __init__(self, name: str, price: float, category: Category):
        self.name = name
        self.price = price
        self.category = category

class Inventory:
    def __init__(self, product: Products, quantity: int):
        self.product = product
        self.quantity = quantity

class Sell:
    def __init__(self, ItensSold: Products, salesperson: str, buyer: str, quantitySold: float, date = datetime.now()):
        self.ItensSold = ItensSold
        self.salesperson = salesperson
        self.buyer = buyer
        self.quantitySold = quantitySold
        self.date = date

class Suplier:
    def __init__(self, name:str, businessNumber: str, telephoneNumber: str, category: str):
        self.name = name
        self.businessNumber = businessNumber
        self.telephoneNumber = telephoneNumber
        self.category = category

class Person:
    def __init__(self, name: str, telephoneNumber: str, SINumber: str, email: str, address: str):
        self.name = name
        self.telephoneNumber = telephoneNumber
        self.SINumber = SINumber
        self.email = email
        self.address = address

class Employee(Person):
    def __init__(self, employeeNumber: str, name: str, telephoneNumber:str, SINumber: str, email: str, address: str):
        self.employeeNumber = employeeNumber
        super(Employee, self).__init__(name, telephoneNumber, SINumber, email, address)
