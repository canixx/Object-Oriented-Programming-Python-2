class Cars():
    def __int__(self, model, price):
        self.model = model
        self.price = price


class Gas():
    def gas_detail(self):
        print("Araba benzinli.")

    def info_gas(self):
        print("Çok yakar...")


class Diesel():
    def diesel_detail(self):
        print("Araba dizel.")

    def info_diesel(self):
        print("Çok para...")


class Electric():
    def electric_detail(self):
        print("Araba elektrikli.")

    def info_electric(self):
        print("Tork ...")


class Mercedes(Cars,Gas):
    def __init__(self, model, price):
        Cars.__init__(self,model, price)
        Gas.__init__(self)

    def info_mercedes(self):
        print("Model: ", self.model, "\nPrice:", self.price)


class Bmw(Cars, Gas, Diesel, Electric):
    pass


class Togg(Cars, Gas, Diesel, Electric):
    pass


meso = Mercedes("CLA180", 5555)

meso.info_mercedes()