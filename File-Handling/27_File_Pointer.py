# FILE POINTER:-

# It is like the blinking cursor in text editor.
# When we open a file the pointer is at the beginning (index 0)
# As reading progress the pointer moves 

# to methods to handle this:-
# 1) tell() :- to find the pointer
# 2) seek() :- to move the pointer



# tell() :-

# with open("example.txt" , "w") as f:
#     print(f.tell())
#     f.write("Hello Good Morning")
#     print(f.tell())
    
# O/P =>
# 0
# 18



# seek() :-

# file_object.seek(offset , whence)
#    .offset -> How many bytes to move
#    .whence (optional)
#          0: start of the file(default)
#          1: current position of the pointer
#          2: End of the file

# with open ('example.txt' , 'r') as f:
#     print(f.tell())
#     print(f.read())
#     print(f.tell())
#     print(f.read())
#     # O/P => 
#     # 0
#     # Hello Good Morning
#     #                       (Blank line is here)   (not printing the last f.read() because the current position of the pointer is last of the file)
    
#     f.seek(0)
#     print(f.read())
#     # 0
#     # Hello Good Morning
#     # 18
#     #                       (Blank line is here)
#     # Hello Good Morning



# with open ("test.bin" , 'wb') as f:
#     f.write(b'ABCDEFGHIJ')
# with open('test.bin','rb') as f:
#     f.seek(3)
#     print(f.read(1))    # b'D'
#     f.seek(2,1)
#     print(f.read())     # b'GHIJ'
#     print(f.read(2))    # b'' (as cursor is at last position)
#     f.seek(-5,2)
#     print(f.read(1))    # b'F'
    
