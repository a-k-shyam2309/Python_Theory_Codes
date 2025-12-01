def Calculator():
    print("Enter any one according to your need given below:")
    print("Addition : add")
    print("Subtraction : sub")
    print("Multiplication : mul")
    print("Division : div")
    print("Modulus : mod")
    str = input("Enter Your Choice: ")
    a = int(input("Enter 1st Numbers: "))
    b = int(input("Enter 2nd Numbers: "))
    if (str == "add"):
        print(a+b)
    elif (str == "sub"):
        print(a-b)
    elif (str == "mul"):
        print(a*b)
    elif (str == "div"):
        if (b == 0):
            print("Division with zero is not possible.")
        else:
            print(a/b)
    elif (str == "mod"):
        if (b == 0):
            print("Division with zero is not possible.")
        else:
            print(a%b)
    else:
        print("Entered an invalid Operator.")

Calculator()