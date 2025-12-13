filename = "data.txt"

try:
    with open (filename , "r") as f:
        line = f.read()
        print("Opened Successfully")
        print(line)
except FileNotFoundError:
    print("Error: File Not") 