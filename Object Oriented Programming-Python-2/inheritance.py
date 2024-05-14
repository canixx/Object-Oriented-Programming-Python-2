class Animal: #parent
    def __init__(self):
        print("animal is created")

    def toString(self):
        print("animal")

    def walk(self):
        print("animal walk")

class Monkey(Animal):  #child
    def __init__(self):
        super().__init__()  #parent classın initini child classa aktarmamızı sağlar.
        print("monkey is created")

    def toString(self):
        print("monkey")

    def climb(self):
        print("monkey can climb")

class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")

    def fly(self):
        print("fly")

m1 = Monkey()
m1.toString() #monkey classındaki toStringi print eder.
m1.walk()
m1.climb()
print("------------------")
b1= Bird()
b1.walk()
b1.toString() #bird classında toString olmadığı için animal classındakini print eder.
b1.fly()
b1.climb() #çalışmaz
