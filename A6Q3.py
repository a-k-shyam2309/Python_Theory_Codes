
class College:
    def __init__(self):
        self.P1 = Person("Male")
        self.P2 = Person("Female")

class Person:
     def __init__ (self , gender):
         self.gender = gender

C1 = College()
print(C1.P1.gender)
print(C1.P2.gender)