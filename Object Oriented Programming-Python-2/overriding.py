#geçersiz kılma olarak adlandırılır

class Animal:

    def toString(self):  #classın hangi class oldugunu dönecek bize.
        print("animal")

class Monkey(Animal):

    def toString(self):
        print("monkey")

a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString() #hangi toStringi çağıracak? kendine ait olanı çağırıyor. yani monkeyin toStringi,
              # animalin toStringini override ediyor/geçersiz kılıyor.

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%s, %s)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

