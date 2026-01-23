# # CHECKING FOR A VALID PASSWORD USING RE MODULE
# import re
# pswd = input("Enter a password: ")
# pat1 = r'[\w\W]{8,}'
# pat2 = r'[A-Z]'
# pat3 = r'[a-z]'
# pat4 = r'[0,9]'
# pat5 = r'[@ # $ & * +]'
# if (re.match(pat1 , pswd) and re.search(pat2 , pswd) and re.search(pat3 , pswd) and re.search(pat4 , pswd) and re.search(pat5 , pswd)):
#     print("Valid Password")
# else:
#     print("Invalid Password")
    


# NOW CHECKING FOR A VALID PASSWORD USING RE MODULE AND ALSO SHOWING WHY PASSWORD FAILS TO MEET THE CRITERIA
# import re
# pswd = input("Enter a password: ")
# pat1 = r'[\w\W]{8,}'
# pat2 = r'[A-Z]'
# pat3 = r'[a-z]'
# pat4 = r'[0,9]'
# pat5 = r'[@ # $ & * + %]'

# if (re.match(pat1 , pswd)):
#     if (re.search(pat2 , pswd)):
#         if (re.search(pat3 , pswd)):
#             if (re.search(pat4 , pswd)):
#                 if (re.search(pat5 , pswd)):
#                     print("Valid Password")
#                 else:
#                     print("Invalid Password, Please enter a special symbol")
#             else:
#                     print("Invalid Password, Please enter a digit")
#         else:
#                     print("Invalid Password, Please enter a Lower Case")
#     else:
#                     print("Invalid Password, Please enter a Upper Case")
# else:
#                     print("Invalid Password, Please enter of minimum length 8")


# # CHECKING FOR A VALID PAN NUMBER
# import re
# pan_no = input("Enter ur pan number: ")
# pat1 = r'\w{10}'
# pat2 = r'[A-Z]{5}'
# pat3 = r'\d{4}'
# pat4 = r'[A-Z]{1}'

# if (re.match(pat1 , pan_no) and re.search(pat2 , pan_no) and re.search(pat3 , pan_no) and re.search(pat4 , pan_no)):
#     print("Valid Pan Number")
# else:
#     print("Invalid Pan Number")
