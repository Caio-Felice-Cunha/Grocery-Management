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
            sold.append(Sell(Products(i[0], i[1], i[2]), i[3], i[4], i[5]))
        return sold