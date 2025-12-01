# CHECKING FOR A VALID PASSWORD USING RE MODULE
import re
def check_Valid_Pswd(s):
    pat1 = r'[\w\W]{8,}'
    pat2 = r'[A-Z a-z]'
    pat3 = r'[0,9]'
    pat4 = r'[@#$&*+]'
    if (re.fullmatch(pat1 , s) and re.search(pat2 , s) and re.search(pat3 , s) and re.search(pat4 , s)):
        print("Valid Password")
    else:
        print("Invalid Password")

str = input("Enter a password: ")
check_Valid_Pswd(str)