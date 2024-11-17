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

        inventory = DaoInventory.read()

        inventory = list(map(lambda x: Inventory(Products(x.product.name, x.product.price, "Category not defined"), x.quantity) if(x.product.category == categoryToRemove) else(x), inventory))

        with open('inventory.txt', 'w') as arc:
            for i in inventory:
                arc.writelines(i.product.name + "|"
                               + i.product.price + "|"
                               + i.product.category + "|"
                               + str(i.quantity))
                arc.writelines('\n')

    def alterCatergory(self, categoryToAlter, categoryAltered):
        x = DaoCategory.read()

        cat = list(filter(lambda x: x.category == categoryToAlter, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.category == categoryAltered, x))

            if len(cat1) == 0:
                x = list(map(lambda x: Category(categoryAltered) if(x.category == categoryToAlter) else(x), x ))
                print(f'The category "{categoryToAlter}" was replaced by the new category "{categoryAltered}"')

                inventory = DaoInventory.read()

                inventory = list(map(lambda x: Inventory(Products(x.product.name, x.product.price, categoryAltered), x.quantity) if(x.product.category == categoryToAlter) else(x), inventory))

                with open('inventory.txt', 'w') as arc:
                    for i in inventory:
                        arc.writelines(i.product.name + "|"
                                    + i.product.price + "|"
                                    + i.product.category + "|"
                                    + str(i.quantity))
                        arc.writelines('\n')
 
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
        ordered = []

        for i in sales:
            name = i.ItensSold.name
            quantity = i.quantitySold
            size = list(filter(lambda x: x['product'] == name, products))

            if len(size) > 0:
                products = list(map(lambda x: {'product': name, 'quantity': int(x['quantity']) + int(quantity)} if(x['product'] == name) else(x), products))
            else:
                products.append({'product': name,
                                 'quantity': int(quantity)})
                
        ordered = sorted(products, key=lambda k: k['quantity'], reverse=True)

        print('These are the best selling products')
        a = 1
        for i in ordered:
            print(f'===== Product: [{a}] =====')
            print(f'Product: {i['product']} \n'
                    f'Quantity: {i['quantity']} \n')
            a += 1

    def showSale(self, startDate, endDate):
        sales = DaoSell.read()
        startDate1 = datetime.strptime(startDate, '%d/%m/%Y')
        endDate1 =  datetime.strptime(endDate, '%d/%m/%Y')

        selectedSales = list(filter(lambda x: datetime.strptime(x.date, '%d/%m/%Y') >= startDate1 and datetime.strptime(x.date, '%d/%m/%Y') <= endDate1, sales))

        cont = 1
        total = 0

        for i in selectedSales:
            print(f"===== Sale [{cont}] =====")
            print(f"Name: {i.ItensSold.name}\n"
                  f"Category: {i.ItensSold.category}\n"
                  f"Date: {i.date}\n"
                  f"Quantity: {i.quantitySold}\n"
                  f"Client: {i.buyer}\n"
                  f"Salesperson: {i.salesperson}\n")
            total += int(i.ItensSold.price) * int(i.quantitySold)
            cont += 1
        print(f'Total: {total}')

class ControllerSupplier:
    def registerSupplier(self, name, businessNumber, telephoneNumber, category):
        x = DaoSupplier.read()

        businessNumberList = list(filter(lambda x: x.businessNumber == businessNumber, x))

        telephoneNumberList = list(filter(lambda x: x.telephoneNumber == telephoneNumber, x))

        if len(businessNumberList) > 0:
            print(f"This business number {businessNumber} already exist")
        elif len(telephoneNumber) > 0:
            print(f"This telephone number {telephoneNumber} already exist")
        else:
            if len(businessNumber) == 14 and len(telephoneNumber) <= 11 and len(telephoneNumber) >= 10:
                DaoSupplier.save(Supplier(name, businessNumber, telephoneNumber, category))
            else:
                print("Type a valid business number or a telephone number")

    def alterSupplier(self, alterName, newName, newBusinessNumber, newTelephoneNumber, newCategory):
        x = DaoSupplier.read()

        inv = list(filter(lambda x: x.name == alterName, x))

        if len(inv) > 0:
            inv = list(filter(lambda x: x.businessNumber == newBusinessNumber, x))

            if len(inv) == 0:
                x = list(map(lambda x: Supplier(newName, newBusinessNumber, newTelephoneNumber, newCategory) if(x.supplier.name == newName) else(x), x))#########################

            else:
                print(f'This business number {newBusinessNumber}, already exists')
        
        else:
            print(f'The supplier {alterName} that you want to alter, does not exists')

        with open('supplier.txt', 'w') as arc:
            for i in x:
                arc.writelines


    def removeSupplier(self, name):
        x = DaoSupplier.read()

        inv = list(filter(lambda x: x.name == name, x))

        if len(inv) > 0:
            for i in range(len(x)):
                if x[i].name == name:
                    del x[i]
                    break

        else:
            print(f'The supllier {name}, that you want to remove does not exist')
            return None 
        
        with open('supplier.txt', 'w') as arc:
            for i in x:
                arc.writelines(i.name + "|"
                               + i.businessNumber + "|"
                               + i.telephoneNumber + "|"
                               + str(i.category))
                arc.writelines('\n')
            
            print(f'Supplier {name} successfully removed')

    def showSuppliers(self):
        suppliers = DaoSupplier.read()
        if len(suppliers) == 0:
            print('Suppliers list is empty')

        for i in suppliers:
            print("========== Suppliers ==========")
            print(f"Category provided: {i.category}\n"
                  f"Name: {i.name}\n"
                  f"Telephone Number: {i.telephoneNumber}\n"
                  f"Business Number: {i.businessNumber}\n")

class ControllerClient:
    def registerClient(self, name, telephoneNumber, SINumber, email, address):
        x = DaoPerson.read()

        SINumberList = list(filter(lambda x: x.SINumber == SINumber, x))
        if len(SINumberList) > 0:
            print(f'SINumber {SINumber} already exist')
        
        else:
            if len(SINumber) == 9 and len(telephoneNumber) >= 10 and len(telephoneNumber) <= 11:
                DaoPerson.save(Person(name, telephoneNumber, SINumber, email, address))
                print(f'Client {name} successfully registered')
            else:
                print('Telephone number or SINumber not valid')

    def alterClient(self, nameToAlter, newName, newTelephoneNumber, newSINumber, newEmail, newAddress):
        x = DaoPerson.read()

        inv = list(filter(lambda x: x.name == nameToAlter, x))
        if len(inv) > 0:
            x = list(map(lambda x: Person(newName, newTelephoneNumber, newSINumber, newEmail, newAddress) if(x.name == nameToAlter) else(x), x ))
        else:
            print('The clientthat you want to alter does not exist')

        with open('çlients.txt', 'w') as arc:
            for i in x:
                arc.writelines(i.name + "|"
                               + i.newTelephoneNumber  + "|"
                               + i.SINumber  + "|"
                               + i.email  + "|"
                               + i.address)
                arc.writelines('\n')
            print(f'Client {nameToAlter} successfully altered to {newName}')

    def removeClient(cls, name):
        x = DaoPerson.read()

        inv = list(filter(lambda x: x.name == name, x))

        if len(inv) > 0:
            for i in range(len(x)):
                if x[i].name == name:
                    del x[i]
                    break 

        else:
            print('The client {name} that you want to alter does not exist')
            return None 
        
        with open('clients.txt', 'w') as arc:
            for i in x:
                arc.writelines(i.name + "|"
                               + i.telephoneNumber + "|"
                               + i.SINumber + "|"
                               + i.email + "|"
                               + i.adress)
            print('Client {name} successfully removed')

    def showClients(self):
        clients = DaoPerson.read()

        if len(clients) == 0:
            print('The clients list is empty')

        for i in clients:
            print('===== Client =====')
            print(f"Name: {i.name}\n"
                  f"Phone Number: {i.telephoneNumber}\n"
                  f"Adress: {i.adress}\n"
                  f"E-mail: {i.email}\n"
                  f"SINumber: {i.SINumber}"
                  )

class ControllerEmployee:
    def registerEmployee(self, employeeNumber, name, telephoneNumber, SINumber, email, address):
        x = DaoEmployee.read()

        employeeNumberList = list(filter(lambda x: x.employeeNumber == employeeNumber, x))
        SINumberList = list(filter(lambda x: x.SINumber == SINumber, x))

        if len(SINumberList) > 0:
            print(f"This SIN {SINumber} alreaty exist")
        elif len(employeeNumberList) > 0:
            print(f'This employee number {employeeNumber} already exist')
        else:
            if len(SINumber) == 11 and len(telephoneNumber) >= 10 and len(telephoneNumber) <= 11:
                DaoEmployee.save(Employee(employeeNumber, name, telephoneNumber, SINumber, email, address))
                print('Employee {name} successfully registered')
            else:
                print("Type a valid SIN or valid Telephone Number")

    def alterEmployee(self, nameToAlter, newEmployeeNumber, newName, newTelephoneNumber, newSINumber, newEmail, newAdress):
        x = DaoEmployee.read()

        inv = list(filter(lambda x: x.name == nameToAlter, x))

        if len(inv) > 0:
            x = list(map(lambda x: Employee(newEmployeeNumber, newName, newTelephoneNumber, newSINumber, newEmail, newAdress) if(x.name == nameToAlter) else(x), x))

        else:
            print(f'The employee {newName} already exists')

        with open('employees.txt', 'w') as arc:
            for i in x:
                arc.writelines(i.employeeNumber + "|"
                               + i.name + "|"
                               + i.telephoneNumber + "|"
                               + i.SINumber + "|"
                               + i.email + "|"
                               + i.address)
            print(f'Employee {newName} successfully altered')

    def removeEmployee(self, name):
        x = DaoEmployee.read()

        inv = list(filter(lambda x: x.name == name, x))
        if len(inv) > 0:
            for i in range(len(x)):
                if x[i].name == name:
                    del x[i]
                    break

        else:
            print(f'The employee {name} that you want to remove does not exist')
            return None 
        
        with open('employees.txt', 'w') as arc:
            for i in x:
                arc.writelines(i.name  + "|"
                               + i.telephoneNumber + "|"
                               + i.SINumber + "|"
                               + i.email + "|"
                               + i.address
                               )
                arc.writelines('\n')

            print(f'Employee {name} sucessfully removed')

    def showEmployee(self):
        employee = DaoEmployee.read()

        if len(employee) == 0:
            print('Employees list empty')
        
        for i in employee:
            print("===== Employee =====")
            print(f"Name: {i.name}\n"
                  f"Phone Number: {i.telephoneNumber}\n"
                  f"Adress: {i.adress}\n"
                  f"E-mail: {i.email}\n"
                  f"SINumber: {i.SINumber}\n"
                  f"Employee Number: {i.employeeNumber}\n"
                  )
        