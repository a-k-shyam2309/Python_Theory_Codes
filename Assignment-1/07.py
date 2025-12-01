
str = " hello, world! python."
str1 = str.replace("," , "")
str2 = str1.replace("!" , "")
str3 = str2.replace("." , "")

list1 = str3.split()
list1.sort(reverse=True)

str4 = "-".join(list1)
print(str4)