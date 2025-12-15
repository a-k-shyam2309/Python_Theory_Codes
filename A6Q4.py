class Car:
    def __init__(self , make , model):
        self.make = make
        self.model = model
    def getter(self):
        return self.make , self.model
    def setter(self , make , model):
        self.make = make
        self.model = model

c1 = Car("Fortuner" , 2024)
c2 = Car(None , None)

print(c1.getter())
c2.setter("Scorpio" , 2025)
print(c2.getter())