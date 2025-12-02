#  MAP :-

# -> it resolves the iterables value one by one and perform operations according to the function.
# syntax :- map(fun , iterable)
# lazy function so we will use list()


# map only
# nums = [1,2,3,4,5]
# def add(a):
#     return a+100
# squares = list(map(add , nums))				# map
# print(squares)


# lambda + map
# nums = [1,2,3,4,5]
# squares = list(map(lambda x: x*x , nums))		# lambda & map
# print(squares)


# List comprehension + lambda + map
# a = [i+10 for i in range(10)]					# List Comprehension
# squares = list(map(lambda x: x*x , a))  		# lambda & map
# print(squares)
