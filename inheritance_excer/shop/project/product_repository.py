from project.drink import Drink
from project.food import Food

class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self,product_name):
        for pr in self.products:
            if pr.name == product_name:
                return pr

    def remove(self,product_name):
        for pr in self.products:
            if pr.name == product_name:
                self.products.remove(pr)

    def __repr__(self):
        result = '\n'.join(f"{pr.name}: {pr.quantity}" for pr in self.products)
        return result

