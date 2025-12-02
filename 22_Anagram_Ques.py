
# Anagran means same alphabets with different arrangement or positioning.
#ex - sonali & saloni

#method-1
# def check_anagram(s1 , s2):
#     if (len(s1) != len(s2)):
#         return False
#     else:
#         for i in s1:
#             c=0
#             for j in s2:
#                 if i == j:
#                     c+=1
#             if c!=1:
#                 return False
#     return True
# s1 = "saloni"
# s2 = "sonali"
# print(check_anagram(s1,s2))


#method-2
# def check2(s1 , s2):
#     sum1 = 0 
#     sum2 = 0 
#     i=0
#     j=True
#     while j==True:
#         sum1 = int(ord (s1[i]))+sum1
#         sum2 = int(ord (s2[i]))+sum2
#         i = i+1
#         if i == len(s1):
#             j = False
#     if sum1 == sum2:
#         return True
#     else:
#         return False
# s1 = "saloni"
# s2 = "sonali"
# print(check2(s1,s2))


#method-3 (BEST WAY)
# s1 = "silent"
# s2 = "listen"

# if (len(s1) != len(s2)):
#     print("Not Anagram")
# else:
#     l = list(s2)
#     for ch in s1:
#         if ch in l:
#             l.remove(ch)
#     if len(l) == 0:
#         print("Anagram")
#     else:
#         print("Not Anagram")
        
