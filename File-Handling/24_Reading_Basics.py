# Learning about READING in File Handling



# METHOD-1
# f = open("data0.txt","r")
# content = f.read()
# print(content)
# f.close() 



# METHOD-2
# PREFERRED AND SAFE WAY
# with open("data0.txt" , "r") as f:
#     content = f.read()
#     print(content)
# File automatically closed



# METHOD-3
# with open("data0.txt" , "r") as f1:
#     for line in f1:
#         print(line.strip())     # if we write simply then it will create a spce between every line so we will use strip() method.



# METHOD-4
# with open ("data0.txt","r") as f:
#     content = f.readlines()      # It returns a list
#     print(content)