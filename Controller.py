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

a = ControllerCategory()
a.showCategory()
