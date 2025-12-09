# STRUCT :-

# The struct module is the bridge between python's high level objects (integrs,strings) and the raw binary data.
# It's needed to work with binary files, network packets.
# The core concept :
#       1) packaging - converting python values -> bytes(to save in disc or over network).
#       2) unpacking - converting bytes -> Python values (to read and use in code).


# format String :-
# It tells python how to deal with the data.

# (table)
# format        Python Type     Standard Size

    # i             Integer          4 byte
    # f             float            4 byte
    # d             Double           8 byte
    # c             Character        1 byte
    # s             char[]           variable
    # ?             bool             1 byte



# Byte Order (endiannes) :-
# Computer stores bytes/data in the different order. It need to specified before use.

# (table)
# Character           Byorder          Use Case

#     <            little-Endian    Intel/AMD processor
#     >             Big-Endian      Netowrk protocals
#     @               Native            Default




# import struct
# format = '<if1s'
# binary_data = struct.pack(format,10,2.5,b'A')
# print(f"Raw Binary looks like: {binary_data}")

# unpack_data = struct.unpack(format,binary_data)
# print(f"Unpacked output: {unpack_data}")

# O/P =>
# Raw Binary looks like: b'\n\x00\x00\x00\x00\x00 @A'
# Unpacked output: (10, 2.5, b'A')




# import struct 
# size = struct.calcsize("<ifds")
# print(size)

# O/P =>
# 17
