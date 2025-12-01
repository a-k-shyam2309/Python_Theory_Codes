
def Encryption(str):
    list1 = []
    for i in str:
        list1.append(i)
    list1 = list1[::-1]
    for i in range(len(list1)-1):
        list1[i] , list1[i+1] = list1[i+1] , list1[i]
    str1 = "".join(list1)
    print(str1)

def Decryption(str):
    print(str)

str = "Hello"
Encryption(str)
Decryption(str)