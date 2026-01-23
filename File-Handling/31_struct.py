
# import struct
# import sys
# number = 0X12345678
# big_endian = struct.pack('>i' , number)
# print(f"Big Endian: {big_endian}")
# little_endian = struct.pack('<i' , number)
# print(f"Little Endian: {little_endian}")
# print(sys.byteorder)   # It is showing for the system's endian
# O/P =>
# Big Endian: b'\x124Vx'
# Little Endian: b'xV4\x12'
# little



# import pickle 
# user_data = {
#     'name' : "Sunil",
#     'scores' : {90,80,85},
#     "isactive" : True ,
#     'profile' : {'role' : "Teach" , "level" : 5}
# }
# filename = "user_data.pkl"
# with open (filename , "wb") as f:
#     pickle.dump(user_data , f)
#     print("Data successfully picked to file")
    
# with open (filename , "rb") as f:
#     saved_data = pickle.load(f)
#     print("\nData retrived")
#     print(saved_data)
    
# Data successfully picked to file

# Data retrived
# {'name': 'Sunil', 'scores': {80, 90, 85}, 'isactive': True, 'profile': {'role': 'Teach', 'level': 5}}
