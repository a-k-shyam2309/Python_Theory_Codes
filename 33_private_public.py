# Private and Public Variables#


# Private Variables:-
# Private variable can only be accessed within the class.


# class odd:
#     def __init__ (self):
#         self.x = 10
#         self.y = 20
#         self.__z = 30       # z is a private variable
        
#     def prt(self):
#         print("x: " , self.x)
#         print("y: " , self.y)
#         print("z: " , self.__z)
# obj = odd()
# print("x: " , obj.x)
# print("y: " , obj.y)
# # print("z: " , obj.__z)    # It will give error as it is private

# obj.prt()       # It will print value of z too because it is declared in that class only.



# We can give value to the private value from outside the class but can't access it directly.
# class odd:
#     def __init__ (self ,x,y,z):
#         self.x = x
#         self.y = y
#         self.__z = z      # z is a private variable
#     def prt(self):
#         print("x: " , self.x)
#         print("y: " , self.y)
#         print("z: " , self.__z)
        
# obj = odd(2,3,4)
# print("x: " , obj.x)
# print("y: " , obj.y)
# # print("z: " , obj.__z)    # It will give error as it is private

# obj.prt()       # It will print value of z too because it is declared in that class only.


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Private Methods:- 
# A private method can't be called directly from outside the class but can be used in another method and that method can be called.Just similar concept to private variable(can be used inside but not outside).


# class Bank:
#     def __init__ (self , balance):
#         self.__balance = balance
#     def __calculateinterest(self):
#         return self.__balance * 0.05
#     def calculateAmount(self):
#         interest = self.__calculateinterest()
#         return self.__balance + interest
# acc = Bank(10000)
# print(acc.__calculateinterest())          # This will show error as it is a private function
# print(acc.__balance)                      # This will show error as it is a private variable
# print(acc.calculateAmount())              # This will show the answer as it is a public function

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# NOTE :
#  var => public
#  _var => protected
#  __var => private

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++