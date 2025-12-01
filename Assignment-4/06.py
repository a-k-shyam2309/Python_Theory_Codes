import re

def begins(text):
    pat = r'[a-z]+[0-9]+$'
    if (re.fullmatch(pat,text)):
        return "Pass"
    else:
        return "Fail"

print(begins("abc123"))
print(begins("Abc123"))
print(begins("a1b3"))
print(begins("dguysd15766876safdsa23"))
print(begins("dgsd123"))
