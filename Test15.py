

from re import match,findall,sub
# pattern = r'\d\d-\d\d\d\d\d\d\d\d\d\d$' #$ symbol is used to stop the more no of digits otherwise it will show true for more than 5 d       igit number
# s = input("Enter the Phone Number")
# if (match(pattern , s)):
#     print("Valid Number")
# else:
#     print("Invalid Answer")
    
    
    
# email = r'\w+@+\w+.+\w' #  By using plus we can add any number of letters
# a = input("Enter the mail : ")
# if (match(email , a)):
#     print("Valid Mail")
# else:
#     print("Invalid Mail")
    
    
# userid = r'[\w\._]+\@[a-z]+\.[a-z]'
# b = input("Enter the mail : ")
# if (match(userid , b)):
#     print("Valid id")
# else:
#     print("Invalid id")


text = "call me at 9173826735 or at 0669-234567 or mail me at aditya@gmail.com"

phno = r'\d{10}'
landno = r'\d{2,4}-\d{4,6}'
email = r'[\w\._]+\@[a-z]+\.[a-z]+'

result1 = findall(phno , text)
print(result1)
result2 = findall(landno , text)
print(result2)
result3 = findall(email , text)
print(result3)

replacement = input("enter a new Number: ")
result4 = sub(phno , replacement , text)
print(result4)