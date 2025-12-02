
# Finding the values of PI using a formula
# def find_Pi(n):
#     j=2
#     for i in range(1,n):
#         p = 3+((-1)**(i+1))*4/((j)*(j+1)*(j+2))
#         print("The value of Pi is: " , i , p)
#         j = j+2

# find_Pi(3)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# cesar_cipher #

# Method-1

# def shift_char(a):
#     n = ord(a)
#     if (n == 120):
#         n = 97
#     elif (n == 121):
#         n=98
#     elif (n == 122):
#         n=99     
#     elif (n == 88):
#         n = 65
#     elif (n == 89):
#         n=66
#     elif (n == 90):
#         n=67
#     else:
#         n = n+3
#     b = chr(n)
#     return b

# str = "xyz"
# list1 = list(str)
# print(list1)
# list2 = []
# for i in list1:
#     val = shift_char(i)
#     list2.append(val)
# print(list2)


# Method-2

# def cesar_cipher(text , shift):
#     result = ""
#     for ch in text:
#         start = ord('a')
#         index = ord(ch)-start
#         new_index = (index+shift)%26
#         new_char = chr(new_index+start)
#         result += new_char
#     return result
# print(cesar_cipher("hello" , 3))            --> o/p- khoor


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# what if asks for reverse cesar cipher in the question:-

# def reverse_cesar_cipher(text , shift):
#     result = ""
#     for ch in text:
#         start = ord('a')
#         index = ord(ch)-start
#         new_index = (index-shift)%26         #-----> + will change to -
#         new_char = chr(new_index+start)
#         result += new_char
#     return result
# print(reverse_cesar_cipher("khoor" , 3))          --> o/p- hello


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# To find the error using Newton Method
# The formula is :--> 1/2(X_n + (N/X_n))


def newton_method(N,t):
    x_n = N/2
    for i in range (1,10):
        x_new = (0.5)*(x_n+(N/x_n))
        error = abs(x_n - x_new)
        if (error < t):
            return x_new
        x_n = x_new

print(newton_method(2,0.0003))