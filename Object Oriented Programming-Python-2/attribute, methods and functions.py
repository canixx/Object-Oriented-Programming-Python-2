#ATTRIBUTE

class Footballer:

    football_club="Barcelona"
    age = 30

f1= Footballer()

print(f1)
print(f1.age)
print(f1.football_club)

f1.football_club = "Real Madrid"

print(f1.football_club)


#METHODS

class Square(object):

    edge = 5 #meter, class variableı

    def area(self):
        area = self.edge*self.edge #class variableı oldugu icin selfle cagirdik.
        print("Area:", area)

s1 =Square()

print(s1.edge)
print(s1.area())


class Square(object):

    edge = 5 #meter
    area = 0

    def Area(self):
        self.area = self.edge*self.edge
        print("Area:", self.area)

s1 =Square()

print(s1.edge)
print(s1.Area())
s1.edge = 7
s1.Area()


#METHODS VS FUNCTIONS

class Emp(object):

    age = 25
    salary = 1000

    def ageSalaryRatio(self):  #method. class içinde tanımlanır. parametre alır. örneğin self.
        a = self.age / self.salary
        print("method:" ,a)
e1 = Emp()
e1.ageSalaryRatio()

#------------------------------------------------------------------------

def ageSalaryRatio(age, salary): #function. class dışında tanımlanır. Bunun classla bi alakası yoktur.
    a = age / salary
    print("function:", a)


ageSalaryRatio(30,3000)

#--------------------------------------------------------------------------

pi = 3.14
r=5
area = pi*r**2

def findArea(pi,r):  #burada pi ve r parametre. pi yerine a, r yerine b yazabiliriz. sonuç aynıdır.
    area=pi*r**2
    #print(area)
    return area
findArea(pi,r) #burada ise pi ve r fonksiyonun inputları

result1= findArea(pi,r)
result2=findArea(pi,10)  #eğer return yapmazsak result1 ve result2 için konsolda hiçbir şey çıkmaz.
                        #yani fonksiyonun dışarsına çıkartmak için return etmeliyiz.
print(result1+result2)



