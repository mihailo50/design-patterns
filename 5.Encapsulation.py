

class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod # not related to specific object
    def mymethod():
        print("Something...")


p1 = Person('John', 21, 'male')

print(p1.Name)

p1.Name = "Jack"

print(p1.Name)
Person.mymethod()