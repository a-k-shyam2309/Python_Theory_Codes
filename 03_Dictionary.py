# a = {"Aditya":20 , "Rounak":99 , "Arun":85}
# a["Aman"] = 98 
# print(a)

# a.pop("Arun")
# print(a)

# a.popitem()  
# print(a)

# del a["Aditya"]
# print(a)

#O/P =>
# {'Aditya': 20, 'Rounak': 99, 'Arun': 85, 'Aman': 98}
# {'Aditya': 20, 'Rounak': 99, 'Aman': 98}
# {'Aditya': 20, 'Rounak': 99}
# {'Rounak': 99}


# TO ACCESS KEYS FROM A DICTIONARY :-
#  for key in student.keys():            IN-BUILT IS PRESENT
#     print(key)

# TO ACCESS VALUES FROM A DICTIONARY :-
#  for val in student.values():          IN-BUILT IS PRESENT
#     print(val)


# a = {"Aditya":20 , "Rounak":99 , "Arun":85}
# for key,value in a.items():            TO ACCESS BOTH WE CAN USE WRITE LIKE THIS
#     print(key , "-" , value)

#O/P =>
# Aditya - 20
# Rounak - 99
# Arun - 85

