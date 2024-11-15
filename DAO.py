from warnings import catch_warnings
from Models import *

class DaoCategory:
    @classmethod
    def save(cls, category):
        with open('category.txt', 'a') as arc:
            arc.writelines(category)
            arc.writelines('\n')

    @classmethod
    def read(cls):
        with open('category.txt', 'r') as arc:
            cls.category = arc.readlines()

        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))

        cat = []
        for i in cls.category:
            cat.append(Category(i))

        return cat 

class DaoSell:
    @classmethod
    def save(cls, sell: Sell):
        with open('sell.txt', 'a') as arc:
            arc.writelines(sell.ItensSold.name + "|" 
                           + sell.ItensSold.price + "|"
                           + sell.ItensSold.category + "|"
                           + sell.salesperson + "|"
                           + sell.buyer + "|"
                           + str(sell.quantitySold) + "|"
                            + sell.date
                            )
            
            arc.writelines('\n')

    @classmethod
    def read(cls):
        with open('sell.txt', 'r') as arc:
            cls.sell = arc.readlines()

        cls.sell = list(map(lambda x: x.replace('\n', ''), cls.sell))
        cls.sell = list(map(lambda x: x.split('|'), cls.sell))

        sold =[]
        for i in cls.sell:
            sold.append(Sell(Products(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return sold

class DaoInventory:
    @classmethod
    def save(cls, product: Products, quantity):
        with open('inventory.txt', 'a') as arc:
            arc.writelines(product.name + "|"
                           + product.price + "|"
                           + product.category + "|"
                           + str(quantity))
            arc.writelines('\n')

    @classmethod
    def read(cls):
        with open('inventory.txt', 'a') as arc:
            cls.inventory = arc.readlines()

        cls.inventory = list(map(lambda x: x.replace('\n', ''), cls.inventory))

        cls.inventory - list(map(lambda x: x.split("|"), cls.inventory))

        inv=[]
        if len(cls.inventory) > 0:
            for i in cls.Inventory:
                inv.append(Inventory(Products(i[0], i[1], i[2], i[3])))

        return inv
        
class DaoSupplier:
    @classmethod
    def save(cls, supplier = Supplier):
        with open('supplier.txt', 'a') as arc:
            arc.writelines(supplier.name + "|"
                          + supplier.businessNumber + "|"
                          + supplier.telephoneNumber + "|"
                          + supplier.category)
            
            arc.writelines('\n')


    def read(cls):
        with open('supplier.txt', 'r') as arc:
            cls.supplier = arc.readlines()

        cls.supplier = list(map(lambda x: x.replace('\n', ''), cls.supplier))
        cls.supplier = list(map(lambda x: x.split("|"), cls.supplier))

        sup = []
        for i in cls.supplier:
            sup.append(Supplier(i[0], i[1], i[2], i[3]))
        
        return sup

class DaoPerson:
    @classmethod
    def save(cls, people = Person):
        with open('clients.txt', 'a') as arc:
            arc.writelines(people.name  + "|"
                          + people.telephoneNumber + "|"
                          + people.SINumber + "|"
                          + people.email + "|"
                          + people.address)
            
            arc.writelines('\n')

    @classmethod
    def read(cls):
        with open('clients.txt', 'r') as arc:
            cls.clients = arc.readlines()

        cls.clients = list(map(lambda x: x.replace("|", ""), cls.clients))
        cls.clients = list(map(lambda x: x.split("|"), cls.clients))

        cli = []
        for i in cls.people:
            cli.append(Person(i[0], i[1], i[2], i[3], i[4]))

        return cli

class DaoEmployee:
    @classmethod
    def save(cls, employee: Employee):
        with open('employees.txt', 'a') as arc:
            arc.writelines(
                employee.employeeNumber  + "|"
                + employee.name  + "|"
                + employee.telephoneNumber + "|"
                + employee.SINumber + "|"
                + employee.email + "|"
                + employee.address
            )

            arc.writelines('\n')

    @classmethod
    def read(cls):
        with open('employees.txt', 'r') as arc:
            cls.employees = arc.readlines()

            cls.employees = list(map(lambda x: x.replace('\n', ''), cls.employees))
            cls.employees = list(map(lambda x: x.split('|'), cls.employees))

            empl = []
            for i in cls.employees:
                empl.append(Employee(i[0], i[1], i[2], i[3], i[4], i[5]))

            return empl