from project.product import Product

class Drink(Product):
    DEF_QUANTITY = 10

    def __init__(self, name):
        super().__init__(name, self.DEF_QUANTITY)


