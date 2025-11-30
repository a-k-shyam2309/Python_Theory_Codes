
# lambda funciton is use to write the function in a single line
# add = lambda x,y: x+y
# print(add(2,4))
# find1 = lambda a,b : a if (len(a)>len(b)) else b     ---->>>    IF , ELSE STATEMENT FOR LAMBDA FUNCTION


# a=24124
# b=2312
# max1 = lambda x,y : x if (x>y) else y if (x<y) else x+y    ------>>>>    IF , ELSE IF condition FOR LAMBDA FUNCTION (we don't write elif in lambda function)
# val = max1(a,b)
# print(val)



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# reduce() function is used to apply a function cumulatively to the items of an iterable (like a list or tuple), reducing it to a single value.

# import functools              NEED TO IMPORT BEFORE USING REDUCE
#list1 = [1,2,3,4,5]
#sum1 = lambda x,y : x+y
#print(functools.reduce(lambda x,y : x+y ,list1))      ==> REDUCE FUNCTION SYNTAX ==> reduce(func,iterative)



# a = int(input("Enter the Number:"))
# list1 = list(range(1,a+1))
# def mul(a,result):          INSTEAD OF THIS WE CAN ALSO MAKE LABMDA FUNCTION like this  ----->>>   "mul = lambda a , res : a*res"
#     return a*result
# result = functools.reduce(mul,list1)
# print(result)



# import functools
# list = ("mango" , "apple" , "watermelon" , "papaya" , "banana")
# def find (str1 , str2):
#     if (len(str1) > len(str2)):
#         return str1
#     else:
#         return str2
    
# find1 = lambda a,b : a if (len(a)>len(b)) else b        IN THIS WAY A LAMBDA FN CAN BE WRITTEN AT THE PLACE OF SIMPLE FN.

# print(functools.reduce(find1 , list))
