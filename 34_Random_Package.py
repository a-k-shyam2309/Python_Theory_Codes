# THE RANDOM PACKAGE:-

# Built-in python module use for pseudo random numbers.
# Pseudoramdomness :- The numbers generated are not purely random in cosmic random. They are drawn from a sequence that behaves as it were random.
# Distribution :- Random no falls into a specific range and frequenties.
# --> Unifrom distribution:- Every no in the ranges has equal probability of being choosen.
# --> Noraml ditribution:- Numbers cluster around an average (mean) forming a bell curve.


# Functions in Random Package:-
# function                                       Description                                                                 Example

# randint(a,b)                      Return a random integer between a & b(inclusive)                                 dice = random.randint(1,6)
# random()                  Returns a floating point number between 0.0 and 1.0(excluding 1.0)                      chance = random.random()
# uniform(a,b)                   Returns a floating point number between a & b                                      val = random.uniform(1.5,9.5)
# shuffle(list)     Randomly rearranges the elements of a list in place. It doesn't return a new list.                random.shuffle(my_list)
# sample(my_list,k)   Returns a new list containing k unique elements choosen randomly from a list       winners = random.sample(my_list,3)



# import random

# a = random.randint(2,9)
# print(a)

# b = random.random()
# print(b)

# c = random.uniform(2.3 , 4.9)
# print(c)

# lst = [1,4,7,2,6,34,432]

# random.shuffle(lst)
# print(lst)

# e = random.sample(lst , 3)
# print(e)


# Testing random variable:-
# 1) Conformance to Expectation :- If you pick range 0-9 each digit should appear 1/10th of th time.
# 2) Variation :- In a small frequencies won't be prfect. If you flip a coin 100 times, likely to get exactly 50 heads & 50 tails is not possible.
# 3) Law of large numbers :- As the no of trials (N) increases, the result should converge to the expected probability.


# import random 
# def check_randomness(n):
#     hits = [0]*10
#     for i in range(n):
#         a=random.randint(0,9)
#         hits[a]+=1
#     print(hits)
#     for i in range(10):
#         expected = n/10
#         ratio = hits[i]/expected
#         print(f"Number {i} : {hits[i]} (Ratio: {ratio:.3f})")
# check_randomness(100)

# [9, 12, 11, 7, 10, 11, 13, 9, 10, 8]
# Number 0 : 9 (Ratio: 0.900)
# Number 1 : 12 (Ratio: 1.200)
# Number 2 : 11 (Ratio: 1.100)
# Number 3 : 7 (Ratio: 0.700)
# Number 4 : 10 (Ratio: 1.000)
# Number 5 : 11 (Ratio: 1.100)
# Number 6 : 13 (Ratio: 1.300)
# Number 7 : 9 (Ratio: 0.900)
# Number 8 : 10 (Ratio: 1.000)
# Number 9 : 8 (Ratio: 0.800)


# import random
# def find():
#     a = random.randint(1,10)
#     c = 0
#     while(True):
#         n = int(input("Enter Number: "))
#         c+=1
#         if (n>a):
#             print("Too Large, Guess Again...")
#         elif (n<a):
#             print("Too Small, Guess Again...")
#         else:
#             print("You Got Right...")
#             print(f"In {c} times you found the answer...")
#             return False
# find()
