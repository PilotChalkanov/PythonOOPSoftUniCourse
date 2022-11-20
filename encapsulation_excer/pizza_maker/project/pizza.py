from project.dough import Dough
from project.topping import Topping

class Pizza:

    def __init__(self,name:str, dough: Dough, toppings_capacity:int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        if len(value) ==0:
            raise ValueError("The name cannot be an empty string")
        self.__name = value
        return

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value == None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value
        return
    
    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    
    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value
        return

    def add_topping(self,topping:Topping):
        if self.__toppings_capacity <= 0:
            raise ValueError("Not enough space for another topping")
        else:
            if topping.topping_type in self.toppings:
                self.toppings[topping.topping_type] += topping.weight
            else:
                self.toppings[topping.topping_type] = topping.weight
            self.__toppings_capacity -= 1

    def calculate_total_weight(self):
        total_dough_weight = self.dough.weight
        total_toppings_weight = sum([v for v in self.toppings.values()])
        return total_toppings_weight + total_dough_weight


# tomato_topping = Topping("Tomato", 60)
# print(tomato_topping.topping_type)
# print(tomato_topping.weight)
#
# mushrooms_topping = Topping("Mushroom", 75)
# print(mushrooms_topping.topping_type)
# print(mushrooms_topping.weight)
#
# mozzarella_topping = Topping("Mozzarella", 80)
# print(mozzarella_topping.topping_type)
# print(mozzarella_topping.weight)
#
# cheddar_topping = Topping("Cheddar", 150)
#
# pepperoni_topping = Topping("Pepperoni", 120)
#
# white_flour_dough = Dough("White Flour", "Mixing", 200)
# print(white_flour_dough.flour_type)
# print(white_flour_dough.weight)
# print(white_flour_dough.baking_technique)
#
# whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
# print(whole_wheat_dough.weight)
# print(whole_wheat_dough.flour_type)
# print(whole_wheat_dough.baking_technique)
#
# p = Pizza("Margherita", whole_wheat_dough, 2)
#
# p.add_topping(tomato_topping)
# print(p.calculate_total_weight())
#
# p.add_topping(mozzarella_topping)
# print(p.calculate_total_weight())
#
# p.add_topping(mozzarella_topping)

