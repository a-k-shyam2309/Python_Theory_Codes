def first_func(str):
    str = str.lower()
    str1 = []
    for i in str[::-1]:
        str1.append(i)
    str2= "".join(str1)
    if (str2 == str):
        print("Palindrome String.")
    else:
        print("Not a Palindrome String.")


def second_func(str):
    list1 = []
    for i in str:
        if (i==" " or i=="," or i==":"):
            continue
        else:
            if (i.isupper()):
                list1.append(i.lower())
            else:
                list1.append(i)
    list2 = list1[::-1]
    
    
    count=0
    length = len(list1)
    

    for i in range(length):
        if (list1[i] == list2[i]):
            count+=1
        
    if count == length:
        print("Palindrome String.")
    else:
        print("Not a Palindrome String.")
    
 
 
str1 = input("Enter a String: ")
first_func(str1)
second_func(str1)