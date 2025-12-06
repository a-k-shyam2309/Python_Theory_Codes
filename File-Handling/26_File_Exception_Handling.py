# FILE EXCEPTION HANDLING

# Errors might occurs basically due to 3 reasons:-
# 1) The file might be missing.
# 2) The permission may be read only.
# 3) The disk/memory might be full.

# BASIC SYNTAX :- open, close etc perform all the things in the "try" block
# and make "except" block for which errors may arrise.


# try:
#     with open ("test.txt" , "r") as f:        # as we know this file doesn't exist.
#         print(f.read())
# except FileNotFoundError:
#     print("File doesn't Exist")
    



# The Structure try / except / else / finally :-
# try :- The code that might cause error.
# except :- It runs if there is an error.
# else :- It runs if there is no error.
# finally :- Always runs, regardless of success or failure.


# filename="report.txt"
# try:
#     with open(filename, "r") as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print(f"{filename} doesn't Exist")
# except PermissionError:
#     print(f"{filename} is not Accessable")
# else:
#     print(f"{filename} read successfully")
# finally:
#     print("File Operations Finished.")




