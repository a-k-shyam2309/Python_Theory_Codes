decNum = int(input("Enter a Decimal Number: "))

binNum = bin(decNum)
octNum = oct(decNum)
hexNum = hex(decNum)

print()
print(binNum)
print(octNum)
print(hexNum)

# for removing prefix we will use slicing
binNum = binNum[2:]
octNum = octNum[2:]
hexNum = hexNum[2:]

print()
print(binNum)
print(octNum)
print(hexNum)

# to count the number of digits we will use len function
print()
print(len(binNum))
print(len(octNum))
print(len(hexNum))

# again converting them to decimal
# int(string,base)==> REMEMBER THIS FUNCTION
binDec = int(binNum , 2)
octDec = int(octNum , 8)
hexDec = int(hexNum ,16)

print()
print(binDec)
print(octDec)
print(hexDec)
print()