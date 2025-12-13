filename = "student.txt"
list1 = ["abcd" , "asda" , "sdgs" , "erfv" , "aegfew"]

with open (filename , "x") as f:
    for i in list1:
        f.write(i + "\n")

with open (filename , "r") as f:
    print(f.read())