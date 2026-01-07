# LIST COMPREHENSION #

# list1 = [1,2,3,4,5]
# list2 = list1[:]		# using slicing
# list3 = []
# for i in list1:			# using loop method
#     list3.append(i)
# list4 = [j for j in list1]		# using list comprehension
# print(list1)
# print(list2)
# print(list3)
# print(list4)


# lst1 = [2,4,6,8,10]
# lst2 = [i**2 for i in lst1]
# print(lst2)


# a = [i+10 for i in range(10)]
# print(a)




# IF CONDITION IN LIST COMPREHENSION :-
# list1 = [1,2,3,4,5,6,7,8]
# list2 = [j*j for j in list1 if (j%2==0)]  # SQUARING THE EVEN NOS
# print(list2)


# IF-ELSE CONDITION IN LIST COMPREHENSION :-
# list1 = [1,2,3,4,5,6,7,8]
# list2 = ["Even" if (j%2==0) else "odd" for j in list1]   	
# print(list2)


# IF - ELSE-IF CONDITION IN LIST COMPREHENSION :-
# list1 = [1,2,3,4,5,6,7,8]
# list2 = ["Small" if (j<3) else "Mid" if (j<6) else "Large" for j in list1]   	
# print(list2)



# SET COMPREHENSION
s = {x*x for x in range(1, 6)}
print(s)

#O/P:-
{1, 4, 9, 16, 25}
--> Removes duplicates automatically.




# DICTIONARY COMPREHENSION
d = {x: x*x for x in range(1, 6)}
print(d)

#O/P:-
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
--> Key → x, Value → x²





