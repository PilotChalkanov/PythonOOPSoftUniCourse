class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    # def info(self):
    #     print(self.__name)
    #     print(self.__age)

    def get_age(self):
      return self.__age

    def get_name(self):
       return self.__name
    # def set_age(self,age):
    #     self.__age = age

person = Person("George", 32)
print(person.get_name())
print(person.get_age())