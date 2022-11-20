from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self,name:str,budget:int,animal_capacity:int,worker_capacity:int):
        self.name = name
        self.__budget = budget
        self.__animals_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self,animal,price):
        if self.__budget >= price and self.__animals_capacity>0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animals_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animals_capacity > 0 and self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self,worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            self.__workers_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self,worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_animal_expenses = 0
        for animal in self.animals:
            total_animal_expenses += animal.money_for_care
        if self.__budget >= total_animal_expenses:
            self.__budget -= total_animal_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self,amount):
        self.__budget += amount

    def animals_status(self):
        result_str = f"You have {len(self.animals)} animals"
        lion_list = []
        cheetah_list = []
        tiger_list = []
        for animal in self.animals:
            if type(animal) == Lion:
                lion_list.append(animal)
            elif type(animal) == Cheetah:
                cheetah_list.append(animal)
            elif type(animal) == Tiger:
                tiger_list.append(animal)
        result_str += f"\n----- {len(lion_list)} Lions:"
        for lion in lion_list:
            result_str += f"\n{lion.__repr__()}"
        result_str += f"\n----- {len(tiger_list)} Tigers:"
        for tiger in tiger_list:
            result_str += f"\n{tiger.__repr__()}"
        result_str += f"\n----- {len(tiger_list)} Cheetahs:"
        for cheetah in cheetah_list:
            result_str += f"\n{cheetah.__repr__()}"
        return result_str

    def workers_status(self):
        result_str = f"You have {len(self.workers)} workers"
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if type(worker) == Keeper:
                keepers.append(worker)
            elif type(worker) == Caretaker:
                caretakers.append(worker)
            elif type(worker) == Vet:
                vets.append(worker)
        result_str += f"\n----- {len(keepers)} Keepers:"
        for keeper in keepers:
            result_str += f"\n{keeper.__repr__()}"
        result_str += f"\n----- {len(caretakers)} Caretakers:"
        for caretaker in caretakers:
            result_str += f"\n{caretaker.__repr__()}"
        result_str += f"\n----- {len(vets)} Vets:"
        for vet in vets:
            result_str += f"\n{vet.__repr__()}"
        return result_str


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
#
# print(zoo.workers_status())
#
#
