# FILTER #


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


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# lambda + map + filter

# Remember the execution that it will start to solve from inside

# from functools import reduce
# num = [1,2,7,4,3,5,2,6,3]
# print( reduce(lambda x,y : x+y ,list(map(lambda x : x*x ,list(filter(lambda x : x%2==0 , num))))))
