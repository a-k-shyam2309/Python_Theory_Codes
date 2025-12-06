# Learning about WRITING in File Handling



# Appending a Line

# with open("data0.txt" , "a") as f:
#     f.write("\nMy name is Aditya")    # We have append a line in data0.txt
    
# with open ("data0.txt" , "r") as f:     # From this we are printing the lines only.
#     lines = f.read()
#     print(lines)
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
    
#Modifying/Overwriting the whole file by deleting the previous things

# lines = ["4th line" , "5th line" , "6th line" , "7th line"]
# with open("data0.txt" , "w") as f:
#     for l in lines:
#         f.write(l+'\n')
        
# with open ("data0.txt" , "r") as f:
#     print(f.read())

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Creating a new file 

# with open ("example.txt" , "w") as f:           # this file doesn't exist so it will create a new file
#     f.write("This is a brand new file")

# with open ("example.txt" , "r") as f:
#     print(f.read())
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

