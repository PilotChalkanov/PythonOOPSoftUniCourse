class Vet:
    space = 5
    animals = []
    def __init__(self,name):
        self.name = name
        self.animals = []


    def register_animal(self,animal_name):
        if len(self.animals) < Vet.space and len(Vet.animals) < Vet.space :
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)

            return f"{animal_name} registered in the clinic"

        return "Not enough space"

    def unregister_animal(self,animal_name):
        if animal_name in Vet.animals and animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)

            return f"{animal_name} unregistered successfully"

        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space-len(Vet.animals)} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())