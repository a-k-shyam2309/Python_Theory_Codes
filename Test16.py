#TO CHANGE OR REPLACE THE DATE FORMAT USING re MODULE
# from re import sub,match
# text = "Today is 25/11/2025"
# pattern = r'\d{2}+/+\d{2}+/+\d{4}'
# rep = "2025-11-25"
# result = sub(pattern , rep , text)
# print(result)

# text = input("Enter the Number: ")
# pattern = r'[^0-5]\d{9}$' # ^--> Negation --> (It is used to check if first digit is between 0 to 5 it is print invalid)
# if (match(pattern,text)):
#     print("Valid")
# else:
#     print("Invalid")
    
# text = input("Enter the Number: ")
# pattern = r'[0-5]\d{9}$' # ^--> Don't used Negation --> (now in this range only it will valid)
# if (match(pattern,text)):
#     print("Valid")
# else:
#     print("Invalid")


# import re
# text = "1234 xyz 5678 abcd 123 hello 0000 bye"
# pat = r'\d{4}'
# num = re.findall(pat , text)
# print(num)
# #o/p ---> ['1234', '5678', '0000']

# pat1 = re.compile(r"\d{4}")
# num1 = pat1.findall(text)
# print(num1)

# import re
# text = "hello xyz Hello abc hELLO pqr Hello"  # We are extracting hello of different cases
# pat = re.compile(r"hello" , re.IGNORECASE)    # We can also write re.I instead of re.IGNORECASE
# new_text = pat.findall(text)
# print(new_text)


