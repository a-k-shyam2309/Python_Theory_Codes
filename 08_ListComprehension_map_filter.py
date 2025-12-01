# LIST COMPREHENSION #

# list1 = [1,2,3,4,5]
# list2 = list1[:]		# using slicing
# list3 = []
# for i in list1:			# using loop method
#     list3.append(i)
# list4 = [j for j in list1]		# using list comprehension
# print(list1)
# print(list2)
# print(list3)
# print(list4)


# lst1 = [2,4,6,8,10]
# lst2 = [i**2 for i in lst1]
# print(lst2)


# a = [i+10 for i in range(10)]
# print(a)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# IF CONDITION IN LIST COMPREHENSION :-
# list1 = [1,2,3,4,5,6,7,8]
# list2 = [j*j for j in list1 if (j%2==0)]  # SQUARING THE EVEN NOS
# print(list2)


# IF-ELSE CONDITION IN LIST COMPREHENSION :-
# list1 = [1,2,3,4,5,6,7,8]
# list2 = ["Even" if (j%2==0) else "odd" for j in list1]   	
# print(list2)


# IF - ELSE-IF CONDITION IN LIST COMPREHENSION :-
# list1 = [1,2,3,4,5,6,7,8]
# list2 = ["Small" if (j<3) else "Mid" if (j<6) else "Large" for j in list1]   	
# print(list2)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# map():-
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


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# filter():-
# -> it resolves the iterables value one by one and check the condition. If condition satisfies then perform operations according to the function.
# syntax :- filter(fun , iterable)		--> here fun must have condition
# lazy function so we will use list()


# filter only
# def great5(n):
#     if (n > 5):
#         return n
# lst = [11,2,8,3,6,9,4,2,0]
# lst1 = list(filter(great5 , lst))
# print(lst1)


# lambda + filter
# nums = [1,2,3,4,5,6]
# even = list(filter(lambda x : x%2==0 , nums))
# print(even)


# List comprehension + lambda + filter 
# list0 = [12,23,34,45,56,67,78,89,90,10]
# lst1 = [i*2 for i in list0]
# lst2 = list(filter(lambda x: x%2==0 , lst1))
# print(lst2)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# lambda + map + filter
# Remember the execution that it will start to solve from inside

# from functools import reduce
# num = [1,2,7,4,3,5,2,6,3]
# print( reduce(lambda x,y : x+y ,list(map(lambda x : x*x ,list(filter(lambda x : x%2==0 , num))))))



