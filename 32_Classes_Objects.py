# CLASSES AND OBJECTS


# SYNTAX :-

# if we need to keep class empty we need to write pass other it will create error.
# class Car:
#     pass      
# car1 = Car()    # calling by making an object


# Making class with values
# class Car:
#     color="Red"
#     accl=2.5
#     mlg=25
#     brand="Tata"

# car1 = Car()
# print(f"Brand Name: {car1.brand}")
# print(f"Car Color: {car1.color}")
# print(f"Car Acceleration: {car1.accl}")
# print(f"Car Mileage: {car1.mlg}")
# print()
# car1.color = "Blue"
# print(f"Car Modified Color: {car1.color}")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Dog:
#     species = "Indian Desi"
#     def __init__ (self , name , age):
#         self.name = name
#         self.age = age
#     def bark(self):       #SELF IS COMPULSARY WHETHER WE USE IT OR NOT DOESN'T MATTER.
#         return (f"{self.name} says bow bow")
# dog1 = Dog("Sheru" , 5)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  __new__

# It is the constructor that actually ceates the object
# First step in the object creation.
# It allocate memory and returns a new instance of the class.
# It runs before __init__
# It must return the new object instance
# It rarely need implementation because the default method sufficient for creating the object.
# dog2 = Dog("Tommy" , 9)
# print(dog1.name)
# print(dog2.name)
# print(dog2.bark())
# print(dog1.species)
# O/P:-
# Sheru
# Tommy
# Tommy says bow bow
# Indian Desi

# species --> it is a class variable.
# Class Variable :- defined directly inside the class outside of any methods and shared by all objects. 

# name , age is a instance variable.
# Instance Variable :- defined inside any function and used there and not share with other objects.

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Forward reference problem
# if we use class before its declaration then it will give error.

# dog1 = Dog()
# dog1.Bark()
# class Dog:
#     def Bark(self):
#         print("Bhoo")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# From a single class we can call another class and it it not show any error.

# class Dog:
#     def __init__(self):
#         self.cat1=Cat()
# class Cat:
#     def __init__(self):
#         self.dog1=Dog()
        
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  __new__

# It is the constructor that actually ceates the object
# First step in the object creation.
# It allocate memory and returns a new instance of the class.
# It runs before __init__
# It must return the new object instance
# It rarely need implementation because the default method sufficient for creating the object.

# 1) Substring Immutable Types:-
# --> when u want to modufy the immutable class like int , str , float ,tuple etc.
# --> These objects can't be modified after again creation.
# --> and __init__ method is too late to alter the values.
# --> __new__ used to alter the values of the object before their creation.

# 2) Memory Allocation:-
# 
