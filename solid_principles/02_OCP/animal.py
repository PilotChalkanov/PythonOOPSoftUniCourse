from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def animal_sound(self):
        pass

class Cat(Animal):
    def animal_sound(self):
        return 'meow'

class Dog(Animal):
    def animal_sound(self):
        return 'woof-woof'
class Chicken(Animal):
    def animal_sound(self):
        return 'Chick-Chitrik'

cat =Cat()
dog = Dog()
chicken = Chicken()

animals = [cat, dog, chicken]
for animal in animals:
    print(animal.animal_sound())


## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни

