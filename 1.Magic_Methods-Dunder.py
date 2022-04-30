import hashlib

# Dunder -> __init__ or __str__ for ex

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        
        print("Object is being deconstructed.")

p = Person('Mike', 100)

print('#----------------------------------------------------------#')

class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other) -> object:
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"

    def __len__(self):
        pass

    def __call__(self):
        return "Dick"

# v1 = Vector(10, 20)
# v2 = Vector(50, 70)
# v3 = v1 + v2

v3 = hashlib.sha384("1234")

print(v3)
# print(v3())