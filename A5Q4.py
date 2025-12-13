with open("text.txt" , "r") as f:
    lst = f.readlines()
    l = len(lst)
    print("Total no of lines:" , l)
    count1 = 0
    count2 = 0
    for i in lst:
        s = i.split()
        count1 = count1 + len(s)
        count2 = count2 + len(i)
    print("No of words: ",count1)
    print("No of characters: ",count2)