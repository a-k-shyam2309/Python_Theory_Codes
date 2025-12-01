import re
def email_filter(lst):
    pat = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.-]*@[A-za-z]+.[A-Za-z]{2,4}$")
    for i in lst:
        if (pat.fullmatch(i)):
            print(i)
        else:
            print("Not a valid main id")
lst = ["abc@gmail.com" , "12_abc@example.edu" , "A$bc@g17.in" , "xy_129@mail.com"]
email_filter(lst)