class Website:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def loginInfo(self):
        print(self.name + " "+ self.surname)

class Website1(Website):
    def __init__(self, name, surname,ids):
        Website.__init__(self,name,surname)
        self.ids = ids

    def login(self):
        print(self.name + " "+ self.surname + " " +str(self.ids))

class Website2(Website):
    def __init__(self,name,surname,age):
        Website.__init__(self,name,surname)
        self.age = age

    def login(self):
        print(self.name + " "+ self.surname+ " "+ self.age)


p1 = Website("Nazlı", "AYDIN")
p1.loginInfo()
p2 = Website1("Masoud","L-Navıd",1234)
p2.login()
p2.loginInfo()
print(p2.name,p1.name,p2.surname)
p3 = Website2("k","k","24")
p3.loginInfo()
p3.login()