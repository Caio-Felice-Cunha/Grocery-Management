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
        


a = ControllerInventory()
a.removeProduct('banana')
