from itertools import product
from Models import *
from DAO import *
from datetime import datetime

class ControllerCategory:
    def registerCategory(self, newCategory):
        exists = False
        x = DaoCategory.read()

        for i in x:
            if i.category == newCategory:
                exists = True
            
        if not exists:
            DaoCategory.save(newCategory)
            print(f"Category ({newCategory}) registered successfully")

        else:
            print(f"The Category {newCategory}, already exists")


    def removeCategory(self, categoryToRemove):
        x = DaoCategory.read()
        cat = list(filter(lambda x: x.category == categoryToRemove, x))

        if len(cat) <= 0:
            print(f'The category {categoryToRemove}, does not exists')

        else:
            for i in range(len(x)):
                if x[i].category == categoryToRemove:
                    del x[i]
                    break

            print(f"The Category {categoryToRemove}, was successfully removed")

        with open('category.txt', 'w') as arc:
            for i in x:
                arc.writelines(i.category)
                arc.writelines('\n')


    def alterCatergory(self, categoryToAlter, categoryAltered):
        x = DaoCategory.read()

        cat = list(filter(lambda x: x.category == categoryToAlter, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.category == categoryAltered, x))

            if len(cat1) == 0:
                x = list(map(lambda x: Category(categoryAltered) if(x.category == categoryToAlter) else(x), x ))
                print(f'The category "{categoryToAlter}" was replaced by the new category "{categoryAltered}"')
                
            
            else:
                print(f'The category "{categoryAltered}" already exists')

        else:
            print(f'The category "{categoryToAlter}" does not exists')

        with open('category.txt', 'w') as arc:
            for i in x:
                arc.writelines(i.category)
                arc.writelines('\n')

    def showCategory(self):
        categories = DaoCategory.read()

        if len(categories) == 0:
            print('The category is empty')

        else:
            for i in categories:
                print(f'Category: {i.category}')

class ControllerInventory:
    def registerProduct(self, name, price, category, quantity):
        x = DaoInventory.read()
        y = DaoCategory.read()

        h = list(filter(lambda x: x.category == category, y))
        inv = list(filter(lambda x: x.product.name == name, x))

        if len(h) > 0:
            if len(inv) == 0:
                product = Products(name, price, category)
                DaoInventory.save(product, quantity)
                print(f'Product {name} successfully registered')
            
            else: 
                print(f'The product {name} is already registered')
        else:
            print(f'This category {category} does not exist')

    def removeProduct(self, name):
        x = DaoInventory.read()
        
        inv = list(filter(lambda x: x.product.name == name, x))

        if len(inv) > 0:
            for i in range(len(x)):
                if x[i].product.name == name:
                    del x[i]
                    break
            print(f'The product {name} was removed successfully')

        else:
            print(f'The product {name} does not exist')

        with open('inventory.txt', 'w') as arc:
            for i in x: 
                arc.writelines(i.product.name + "|"
                               + i.product.price + "|"
                               + i.product.category + "|"
                               + str(i.quantity))
        

    def alterProduct(self, nameToAlter, newName, newPrice, newCategory, newQuantity):
        x = DaoInventory.read()
        y = DaoCategory.read()

        h = list(filter(lambda x: x.category == newCategory, y))

        if len(h) > 0:
            inv = list(filter(lambda x: x.product.name == nameToAlter, x))
            
            if len(inv) > 0:
                inv = list(filter(lambda x: x.product.name == newName, x))

                if len(inv) == 0:
                    x = list(map(lambda x: Inventory(Products(newName, newPrice, newCategory), newQuantity) if(x.product.name == nameToAlter) else(x), x))

                    print(f'Product {nameToAlter} successfully altered to: {newName, newPrice, newCategory, newQuantity}')
                
                else:
                    print(f'The product {newName} is already registered')
            
            else:
                print(f'The product {nameToAlter} does not exist')

            with open('inventory.txt', 'w') as arc:
                for i in x:
                    arc.writelines(i.product.name + "|"
                                   + i.product.price + "|"
                                   + i.product.category + "|"
                                   + str(i.quantity))
                    
                    arc.writelines('\n')

        else:
            print(f'The category {newCategory} does not exist')

    def showInventory(self):
        inventory = DaoInventory.read()

        if len(inventory) == 0:
            print('Empty inventory')
        else:
            print('======== Products ========')

            for i in inventory:
                print('\n'
                      f'Nome: {i.product.name}\n'
                      f'Price: {i.product.price}\n'
                      f'Category: {i.product.category}\n'
                      f'Quantity: {i.quantity}'
                      )
                
                print('----------')

class ControllerSell:
    def registerSale(self, productName, salesperson, buyer, saleQuantity):
        x = DaoInventory.read()
        temp = []

        exist = False
        quantity = False 

        for i in x:
            if exist == False:

                if i.product.name == productName:
                    exist = True

                    if i.quantity >= saleQuantity:
                        quantity = True
                        i.quantity = int(i.quantity) - int(saleQuantity)

                        sold = Sell(Products(i.product.name, i.product.price, i.product.category), salesperson, buyer, saleQuantity)
                        saleValue = int(saleQuantity) * int(i.product.price)

                        DaoSell.save(sold)

            temp.append(Inventory(Products(i.product.name, i.product.price, i.product.category), i.quantity))

        arc = open('inventory.txt', 'w')
        arc.write("")
    
        for i in temp:
            with open('inventory.txt', 'a') as arc:
                arc.writelines(i.product.name + "|"
                                + i.product.price  + "|"
                                + i.product.category + "|"
                                + str(i.quantity))
                arc.writelines('\n')

        if exist == False:
            print(f'The product {productName} does not exist')
            return None
        elif not quantity:
            print(f'Not enough of {productName} in the inventory.')
            return None
        else:
            print(f'Sale completed successfully')
            return saleValue
        
    def productReport(self):
        sales = DaoSell.read()
        products = []

        for i in sales:
            name = i.ItensSold.name
            quantity = i.quantitySold
            size = list(filter(lambda x: x['product'] == name, products))

            if len(size) > 0:
                products = list(map(lambda x: {'product': name, 'quantity': x['quantity'] + quantity}) if(x['product'] == name) else(x), products)
            else:
                products.append({'product': name,
                                 'quantity': quantity})
                
            ordered = sorted(products, key=lambda k: k['quantity'], reverse=True)

            print('These are the best selling products')

            for i in ordered:
                print(f'===== Product: [{a}] =====')
                print(f'Product: {i['product']} \n'
                      f'Quantity: {i['quantity']} \n')
                a += 1



# a = ControllerInventory()
# a.registerProduct('banana', '5', 'Fruit', '20')
# a.registerProduct('milk', '2', 'Drinks', '30')
# a.registerProduct('hamburger', '25', 'Meats', '80')
# a.registerProduct('pumpkin', '17', 'Vegetables', '6')
# a.registerProduct('water', '34', 'Drinks', '21')

a = ControllerSell()
# a.registerSale('banana', 'joao', 'caio', 10)
