# import copy
# a=[1,2,[3,4],[5,6]]
# b=a
# c=a.copy()
# d=copy.deepcopy(a)
# c[0] == 99
# print(id(a[0]) == id(c[0]))
# d[2][0] = 100
# print(id(a[2][0]) == id(d[2][0]))

# A = [15 , 17 , 3 , 9 , 7]
# print(len(A))
# print(max(A))
# print(min(A))
# print(sum(A))
# print(sum(A)/len(A))
# print(sorted(A))
# print(A)
# str = "python"
# print(sorted(str))

# a = (1,3,5,0)
# for i in reversed(a):
#     print(i)
# print(list(reversed(a)))
# l = [1,5,3,7]
# print(tuple(reversed(l)))

# names= ["Ravi" , "Radha" , "Aman" , "Meera"]
# marks = [80 , 75 , 91 , 87]
# print(list(zip(names,marks)))

# marks.append([10,23,34])
# print(marks)
# marks.remove(87)
# print(marks)

# B = [23,27,76,65,1,90]
# B.sort(reverse = True)
# print(B)

# fruits = ["apple" , "banana" , "kiwi" , "orange" , "kiwo"]
# fruits.sort(key=len , reverse = True)
# print(fruits)
# fruits.sort()    


# animals = ["Cat" , "dog" , "Tiger" , "lion" , "Rhino"]
# animals.sort(key = str.lower)
# print (animals)


# import random
# a = [1,2,3,4,5,6]
# random.shuffle(a)
# print(a)


list1 = []
for i in range(1,101):
    list1.append(i)

list2 =[]
for x in list1:
    count=0
    if x==1:
        continue
    for y in range(2,11):
        if x==y:
            continue
        if x%y==0:
            count+=1

    if count==0:
        list2.append(x)
        
print(list2)