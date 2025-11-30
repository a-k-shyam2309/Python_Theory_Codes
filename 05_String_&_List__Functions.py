# str1 = "Hello"
# str2 = "Section G1"
# str3 = str1 +" "+ str2;
# print(str3)

# text = "Python Programming"
# print("Python" in text)     TRUE
# print("Java" in text)       FALSE


# message = "Good"
# message+="Morning"
# print(message)      GoodMorning

# x = "Python"
# y = "python"
# print(x is y)       False

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

# print(ord("A"))      65
# print(ord("a"))      97
# print(chr(98))       b

# for i in range(65 , 91):
#     print(chr(i) , ": " , i)


# words = ["Python" , "is" , "fun"]
# sentence = "\n".join(words)        ==>  JOIN FUNCTION (we join all the elements of a list using a symbol and make a string)
# sentence = "------".join(words)
# print(sentence)

# sentence = "Python is fun"
# words = sentence.split()           ==> SPLIT FUNCTION (we split all the words (NOT THE DIGITS) of a string and make a list)
# print(words)

# str = "Hello"
# print(str.count("o"))

# letters = list("python")           ==> List Function (stores all the digits in list)
# print (letters) 
#O/P ==> ['p', 'y', 't', 'h', 'o', 'n']

# fruits = ["apple" , "banana" , "watermelon"]
# for i in range(len(fruits)):
#     print(fruits[i] , end = ",")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# zero = [0,1]
# zeros = zero*5
# print(zeros)

# list1 = [10,20,30]
# list2 = list(list1)
# list2[0] = 99
# print(list1)
# print(list2)
#o/p:-
# [10, 20, 30]
# [99, 20, 30]


# list1 = [1,2,3]
# list2 = list1[:]
# list2[0] = 9
# print(list1 , list2)
#o/p:-
#[1, 2, 3] [9, 2, 3]


# list1 = [5,10,15]
# list2 = list1.copy()
# list2.append(20)
# print(list1 , list2)
#o/p:-
#[5, 10, 15] [5, 10, 15, 20]


# import copy
# list1 = [[1,2] , [3,4]]
# list2 = copy.deepcopy(list1)
# list2[0][0] = 99
# print(list1)
# print(list2)
#o/p:-
#[[1, 2], [3, 4]]
# [[99, 2], [3, 4]]


# nums = ['x', 'y', 'z', 'm', 'n', 'o', 'p']
# e_nums = list(enumerate(nums, 1)) #ENUMERATE MAKE LIST OF COLLECTION OF TUPLES OF THE VALUE AND THE NUMBER WE HAVE STARTED FROM.
# print(e_nums)
#o/p:-
# [(1, 'x'), (2, 'y'), (3, 'z'), (4, 'm'), (5, 'n'), (6, 'o'), (7, 'p')]


# letters = ['a' , 'b' ,'c' , 'd' , 'e' , 'f' , 'g' , 'h']
# letters[::2] = ['A' , 'C' , 'E' , 'h'] 
# print(letters)

# colors = ["Red" , "Greeen" , "Blue"]
# colors[:] = ["cyan" , 'mangenta' ,"yellow" , "black"]       # change all the values
# print(colors)

# import copy
# a = [[1,2] , [3,4]]
# b=a
# c = a.copy()
# d = copy.deepcopy(a)
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# print(id(a[0][0])==id(c[0][0])) 
