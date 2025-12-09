# FIXED & VARIABLE LENGTH STRING


# FIXED LENGTH :- 

# Every string is assigned with a predefinde fixed length called max-sixe.
# "Ram" - 3 bytes
# "Ramesh" - 6 bytes
# Max_Size - 20 bytes
# if name < max_size then rest are provided witha null value.
# if name > max_size then name truncated.
# Advantage - faster ascessing
# Disadvantage - not memory efficient


# VARIABLE LENGTH :-
# Every string takes up only as much space it needs.
# And a small marker like; or space is given to indicate.
# A length prefix is given before each string to know the size of the string.
# Advantage - Extremely memory efficient
# Disadvantage - Loose Random Access & become slow

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# FIXED LENGTH CODE :-->

# import struct
# names = ["Rama" , "Ramesh" , "Harish"]
# with open('fixed.bin' , 'wb') as f:
#     for name in names:
#         packed = struct.pack('20s' , name.encode())         # encode() fn will change the string of list to the binary format.
#         f.write(packed)
#         print(f"fixed : {packed} (size:{len(packed)}) bytes")
        
# O/P :- a file is created with name "fixed.bin" and this o/p comes and as we can see it is give 20 bytes to all the names.
# fixed : b'Rama\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' (size:20) bytes
# fixed : b'Ramesh\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' (size:20) bytes
# fixed : b'Harish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' (size:20) bytes



# VARIABLE LENGTH CODE :-->

# import struct
# names = ["Rama" , "Ramesh" , "Harish"]
# with open('variable.bin' , 'wb') as f:
#     for name in names:
#         encoded = name.encode()
#         length = len(encoded)
#         f.write(struct.pack("i" , length))
#         f.write(encoded)
#         print(f"variable: {length} + {name} (total{4+length}bytes)")
        
# O/P :- a file is created with name "variable.bin" and this o/p comes and as we can see it is taking space as per ther name length.
# variable: 4 + Rama (total8bytes)
# variable: 6 + Ramesh (total10bytes)
# variable: 6 + Harish (total10bytes)




# name = 'Sunil'
# encoded = name.encode()
# print(type(name))
# print(type(encoded))
# print(name)
# print(encoded)

# O/P :-
# <class 'str'>
# <class 'bytes'>
# Sunil
# b'Sunil'