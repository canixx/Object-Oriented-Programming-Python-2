#polymorphism çok şekillilik ya da çok biçimlilik demektir.
#superclasstan subclassa aktarılan(inherit edilen) ama subclassta, superclasstan farklı bir şekilde --->
#---->>> kullanılan method varsa buna polymorphism denir.

class Employee:

    def raisee(self):
        raise_rate = 0.1
        return 100 + 100 * raise_rate

class ComputerEng(Employee):

    def raisee(self):  #aslında override ediyor ama zam oranları farklı, yani method aynı ama farklı şekilde kullanılıyor.
        raise_rate = 0.2
        result = 100 + 100*raise_rate
        print("ComputerEng:",result)

class EEE(Employee):

    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100*raise_rate
        print("EEE:",result)


e1 = Employee()
ce = ComputerEng()
eee = EEE()

print("Employee:" , e1.raisee())
ce.raisee()
eee.raisee()

employee_list = [ce,eee]

for employee in employee_list:
    employee.raisee()