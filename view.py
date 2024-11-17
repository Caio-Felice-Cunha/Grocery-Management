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