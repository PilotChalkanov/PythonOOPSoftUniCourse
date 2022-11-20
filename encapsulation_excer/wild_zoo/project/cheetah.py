from project.animal import Animal

class Cheetah(Animal):
    DEF_MONEY = 60
    def __init__(self,name,gender,age):
        super().__init__(name,gender,age,self.DEF_MONEY)