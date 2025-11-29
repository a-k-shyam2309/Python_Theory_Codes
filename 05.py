# str1 = "Hello"
# str2 = "Section G1"
# str3 = str1 +" "+ str2;
# print(str3)

# text = "Python Programming"
# print("Python" in text) 
# print("Java" in text)


# message = "Good"
# message+="Morning"
# print(message)

# x = "Python"
# y = "Python"
# print(x is y)

# str = "Python"
# print(str[0])
# print(str[-6])
# print(str[4])
# print(str[-2])
# print(str[2])
# print(str[-4])

# text = "Hello How Are You"
# print(text[0:4])
# print(text[0:16:3])

# str = "Python"
# print(str[-4:-1])

# print(ord("A"))
# print(ord("a"))

# for i in range(65 , 91):
#     print(chr(i) , ": " , i)

# text = "HELLO"
# encrypted = " "
# for ch in text :            
#     encrypted += chr(ord(ch)+1)
# print(encrypted)

# decrypted = "  "
# for x in encrypted:
#     decrypted+=chr(ord(x)-1)
# print(decrypted)

# words = ["Python" , "is" , "fun"]
# sentence = "\n".join(words)\
# sentence = "------".join(words)
# print(sentence)

# sentence = "Python is fun"
# words = sentence.split()
# print(words)

# str = "Hello"
# print(str.count("o")) 

# letters = list("python")
# print (letters) 

# fruits = ["apple" , "banana" , "watermelon"]
# for i in range(len(fruits)):
#     print(fruits[i] , end = ",")

# zero = [0,1]
# zeros = zero*5
# print(zeros)

# list1 = [10,20,30]
# list2 = list(list1)
# list2[0] = 99
# print(list1)
# print(list2)

# list1 = [1,2,3]
# list2 = list1[:]
# list2[0] = 9
# print(list1 , list2)

# list1 = [5,10,15]
# list2 = list1.copy()
# list2.append(20)
# print(list1 , list2)

# import copy
# list1 = [[1,2,] ,[3,4]]
# list2 = copy.deepcopy(list1)
# list2[0][0] = 99
# print(list1)
# print(list2)


# fruits = ["apple" , "banana" , "watermelon" , "grapes" , "mango"]


# Names = ['x' , 'y' , 'z' , 'm' , 'n' , 'o' , 'p']
# e_fruits = list(enumerate(__name__ames,1))

# letters = ['a' , 'b' ,'c' , 'd' , 'e' , 'f' , 'g' , 'h']
# letters[::2] = ['A' , 'C' , 'E' , 'h'] 
# print(letters)

# colors = ["Red" , "Greeen" , "Blue"]
# colors[:] = ["cyan" , 'mangenta' ,"yellow" , "black"] 
# print(colors)

import copy
a = [[1,2] , [3,4]]
b=a
c = a.copy()
d = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))
print(id(d))

print(id(a[0][0])==id(c[0][0]))
