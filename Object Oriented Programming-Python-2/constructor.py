#initializer or constructor

class Animal(object):

    def __init__(self, a, b):
        self.name = a   #içerdeki obje(self.name) dışardan gelen objeye eşit olmalı (name).
        self.age = b

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

a1 = Animal("dog", 2)
a2 = Animal("cat", 4)
a3 = Animal("bird", 6)
print(a1.getAge())
print(a2.getAge())
print(a3.getAge())
print(a1.getName())
print(a2.getName())
print(a3.getName())



