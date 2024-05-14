"""
-----#abstract classlar, subclass için şablon görevi görür ve kullanılcak ortak fonksiyonları kendi içlerinde tutarlar.

class Animal:
    pass
class Bird(Animal):

a= Animal()  -----#bu olmaz. Abstract classtan yani Animal classından hiçbir şekilde obje yaratılamaz.
"""

#ABSTARCT CLASSTA KULLANILAN HER ABSTRACTMETHOD SUBCLASSLARDA KULLANILMAK ZORUNDADIR.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self): pass

class Bird(Animal):
    def __init__(self):
        print("bird")

    def walk(self):   #abstract classta var. zorunlu kullanım.
        print("walk")

    def run(self):  #abstractclassta var. zorunlu kullanım.
        print("run")

a = Animal()
b1=Bird()