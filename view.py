from unicodedata import category
import Controller
import os.path


def createFiles(*args): 
    for i in args:
        if not os.path.exists(i):
            with open(i, "w") as arc:
                arc.write("")

# createFiles("clients.txt"
#             , "category.txt"
#             , "employees.txt"
#             , "inventory.txt"
#             , "sell.txt"
#             , "supplier.txt")

if __name__ == "__main__":

    while True:
        local = int(input("Type 1 to access Categories \n"
                          "Type 2 to access Inventory \n"
                          "Type 3 to access Supplier \n"
                          "Type 4 to access Client \n"
                          "Type 5 to access Employee \n"
                          "Type 6 to access Sale \n"
                          "Type 7 to see the top sale products \n"
                          "Type 8 to exit \n"
        ))

        if local == 1:
            cat = Controller.ControllerCategory()
            while True:
                decide = int(input("Type 1 to register a Category \n"
                                    "Type 2 to remove a Category \n"
                                    "Type 3 to alter a Category \n"
                                    "Type 4 to show all the Categories\n"
                                    "Type 5 to exit \n"
                ))

                if decide == 1:
                    category = input("Type the category that you want to register\n")
                    cat.registerCategory(category)

                elif decide == 2:
                    category = input("Type the category the you want to remove\n")
                    cat.removeCategory(category)

                elif decide == 3:
                    category = input("Type the category the you want to alter\n")
                    newCategory = input("Type the new category")
                    cat.alterCatergory(category, newCategory)

                elif decide == 4:
                    cat.showCategory()

                else:
                    break

        elif local == 2: 
            cat = Controller.ControllerInventory()
            while True:
                decide = int(input("Type 1 to register a Product \n"
                                    "Type 2 to remove a Product \n"
                                    "Type 3 to alter a Product \n"
                                    "Type 4 to show the Inventory\n"
                                    "Type 5 to exit \n"
                ))

                if decide == 1:
                    name = input("Type the product name: \n")
                    price = input("Type the product price: \n")
                    category = input("Type the product category: \n")
                    quantity = input("Type the product quantity: \n")
                    cat.registerProduct(name, price, category, quantity)

                elif decide == 2:
                    product = input("Type the product the you want to remove\n")
                    cat.removeProduct(product)

                elif decide == 3:
                    product = input("Type the product the you want to alter\n")
                    newProduct = input("Type the new product")
                    cat.alterProduct(product, newProduct)

                elif decide == 4:
                    cat.showInventory()

                else:
                    break


        elif local == 3: 
            cat = Controller.ControllerSupplier()
            while True:
                decide = int(input("Type 1 to register a Supplier \n"
                                    "Type 2 to remove a Supplier \n"
                                    "Type 3 to alter a Supplier \n"
                                    "Type 4 to show Suppliers\n"
                                    "Type 5 to exit \n"
                ))

                if decide == 1:
                    name = input("Type the Name of the supplier: \n")
                    businessNumber = input("Type the Business Number of the suppier: \n")
                    telephoneNumber = input("Tupe the Telephone Number of the supplier: \n")
                    category = input("Tupe the Category of the supplier: \n")
                    cat.registerSupplier(name, businessNumber, telephoneNumber, category)

                elif decide == 2:
                    supplier = input("Type the name of the supplier that you want to remove: ")
                    cat.removeSupplier(supplier)

                elif decide == 3:
                    alterName = input("Type the name of the supplier that you want to alter: ")
                    newName = input("Type the new name of the supplier: ")
                    newBusinessNumber = input("Type the new business number of the supplier: ")
                    newTelephoneNumber = input("Type the new telephone number of the supplier: ")
                    newCategory = input("Type the new category of the supplier: ")
                    cat.alterSupplier(alterName, newName, newBusinessNumber, newTelephoneNumber, newCategory)
                
                elif decide == 4:
                    cat.showSuppliers()
                
                else:
                    break


        elif local == 4: 
            cat = Controller.ControllerClient()
            while True:
                decide = int(input("Type 1 to register a client \n"
                                    "Type 2 to remove a client \n"
                                    "Type 3 to alter a client \n"
                                    "Type 4 to show clients\n"
                                    "Type 5 to exit \n"
                ))

                if decide == 1: 
                    name  = input("Type the name of the client: \n")
                    telephoneNumber  = input("Type the telephone number of the client: \n")
                    SINumber  = input("Type the SIN number of the client: \n")
                    email  = input("Type the e-mail of the client: \n")
                    address  = input("Type the address of the client: \n")

                    cat.registerClient(name, telephoneNumber, SINumber, email, address)

                elif decide == 2:
                    client  = input("Type the name of the client that you want to remove: \n")

                    cat.removeClient(client)

                elif decide == 3:
                    nameToAlter  = input("Type the name of the client that you want to alter: \n")
                    newName  = input("Type the new name of the client: \n")
                    newTelephoneNumber  = input("Type the new telephone number of the client:: \n")
                    newSINumber  = input("Type the new SIN number of the client:: \n")
                    newEmail  = input("Type the new e-mail of the client:: \n")
                    newAddress  = input("Type the new address of the client:: \n")

                    cat.alterClient(nameToAlter, newName, newTelephoneNumber, newSINumber, newEmail, newAddress)

                elif decide == 4:
                    cat.showClients()

                else:
                    break


        elif local == 5: 
            cat = Controller.ControllerEmployee()

            while True:
                decide = int(input("Type 1 to register a employee \n"
                                    "Type 2 to remove a employee \n"
                                    "Type 3 to alter a employee \n"
                                    "Type 4 to show employee\n"
                                    "Type 5 to exit \n"
                ))

                if decide == 1:

                    employeeNumber = input("Type the Employee Number: \n")
                    name = input("Type the Employee Name: \n")
                    telephoneNumber = input("Type the Employee Telephone Number: \n")
                    SINumber = input("Type the Employee SIN numbwe: \n")
                    email = input("Type the Employee e-mail: \n")
                    address = input("Type the Employee address: \n")

                    cat.registerEmployee(employeeNumber, name, telephoneNumber, SINumber, email, address)

                elif decide == 2:
                    employee = input("Type the employee that you want to remove")
                    cat.removeEmployee(employee)

                elif decide == 3:
                    nameToAlter = input("Type the name of the employee that you want to alter: \n")
                    newEmployeeNumber = input("Type the new Employee Number: \n")
                    newName = input("Type the new Employee Name: \n")
                    newTelephoneNumber = input("Type the new Employee Number: \n")
                    newSINumber = input("Type the new Employee SIN Number: \n")
                    newEmail = input("Type the new Employee E-mail: \n")
                    newAdress = input("Type the new Employee Address \n")

                    cat.alterEmployee(nameToAlter, newEmployeeNumber, newName, newTelephoneNumber, newSINumber, newEmail, newAdress)


                elif decide == 4:
                    cat.showEmployee()

                else:
                    break


        elif local == 6: 
            cat = Controller.ControllerSell()
            while True:
                decide = int(input("Type 1 to make a sale \n"
                                    "Type 2 to show the sales\n"
                                    "Type 3 to exit \n"
                ))

                if decide == 1:
                    productName = input("Type the name of the product: \n")
                    salesperson = input("Type the name of the salesperson: \n")
                    buyer = input("Type the name of the client: \n")
                    saleQuantity = input("Type quantity: \n")

                    cat.registerSale(productName, salesperson, buyer, saleQuantity)


                elif decide == 2:
                    startDate = input("Enter the start date in day/month/year format: \n")
                    endDate = input("Enter the end date in day/month/year format: \n")

                    cat.showSale(startDate, endDate)

                else: break

        elif local == 7: 
            a = Controller.ControllerSell()
            a.productReport()
        
        else:
            break