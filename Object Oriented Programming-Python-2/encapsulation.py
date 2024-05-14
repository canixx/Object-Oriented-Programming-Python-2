#metod ya da variablelara erişimi kısıtlamaktır. doğrudan modifiye etmeyi yani doğrudan erişimi kısıtlamak.

class BankAccount(object):

    def __init__(self,name,money,adress):
        self.name = name #global
        self.__money = money #private
        self.adress = adress

    #get ve set: private memberlara ulaşabilmek için

    def getMoney(self): #global method
        return self.__money

    def setMoney(self,amount): #global method
        self.__money = amount

    def __increase(self): #private method
        self.__money = self.__money+500

p1 = BankAccount("nazlı",1000,"norway")
p2 = BankAccount("aydın", 2000, "finland")

print("get method:",p1.getMoney())
#print(p1.money) #hata verecek.
p1.setMoney(5000)
print("after set method:", p1.getMoney())

#p1.__increase() ---> hata verecek
print("after raise:", p1.getMoney())

