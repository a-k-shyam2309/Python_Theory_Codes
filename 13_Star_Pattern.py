# n = int(input("Enter the no of rows: "))

# for i in range(n):
#     print((i+1)*"*")


# n = int(input("Enter the no of rows: "))

# for i in range(n):
#     r = n-i-1
#     print(r*" " , end = "")
#     print((2*i+1)*"*" , end = "")
#     print(r*" ")    
    
    
# for i in range(n+1):
#     r=n-i+1
#     print(r*" " , i*"*")

# list1 = []
# count=0
# n=1
# while (count<100):
#     k=0
#     if (n<2):
#         print(n , "is a special case")
#         n+=1
#     else:
#         for i in range (2,int(n**0.5)+1):
#             if (n%i == 0):
#                 k+=1
#         if (k==0):
#             print(n , end = " ")
#             count+=1
#             n+=1
#         else:
#             n+=1
            

# def is_Prime(a,b):
#     for n in range(a,b+1):
#         k=0
#         if (n<2):
#             print(n , "is a special case")
#             n+=1
#         else:
#             for i in range (2,int(n**0.5)+1):
#                 if (n%i == 0):
#                     k+=1
#             if (k==0):
#                 print(n , end = " ")
#                 n+=1
#             else:
#                 n+=1

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# is_Prime(a,b)

# list1 = [2,-3,4,6,-5,-7,13,3,-11,-2,9,8]
# l = len(list1)
# for i in range (l):
#     for j in range (i+1,l):
#         if list1[i] > 0 and list1[j] < 0:
#             temp = list1[i]
#             list1[i] = list1[j]
#             list1[j] = temp
# print(list1)

# list1 = [2,-3,4,6,-5,-7,13,3,-11,-2,9,8]
# def partion(list1):
#     n = len(list1)
#     neg = 0
#     for i in range(n):
#         if (list1[i]<0):
#             T = list1[i]
#             j=i
#             while j>neg:
#                 list1[j] = list1[j-1]
#                 j-=1
#             list1[neg] = T
#             neg+=1
#     print(list1)

# partion(list1)

