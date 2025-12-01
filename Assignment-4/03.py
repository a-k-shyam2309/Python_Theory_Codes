# import re

# def normallize_phones(lst):
#     # pat = re.compile(r'(?:\+91|0091|91|\(91\))?\s*([\d\s-]{10,15})')
#     rat = r'(?:\+91|0091|\(91\)|91)\s*[-]?\s*(\d{5})[-]?(\d{5})'
#     return re.sub(rat , r'+91-\1\2',lst)

# str1 = "(91)8364747638"
# str2 = "+91-1234567890"
# str3 = "0091 9234567801"
# str4 = "91 9267384670"
# m = normallize_phones(str1)
# n = normallize_phones(str2)
# a = normallize_phones(str3)
# b = normallize_phones(str4)
# print(m)
# print(n)
# print(a)
# print(b)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# import re

# def normallize_phones(lst):
#     # pat = re.compile(r'(?:\+91|0091|91|\(91\))?\s*([\d\s-]{10,15})')
#     rat = r'(\+91|0091|\(91\)|91)\s*[-]?\s*(\d{5})[-]?(\d{5})'
#     return re.sub(rat , r'+91-\2\3',lst)

# str1 = "(91)8364747638"
# str2 = "+91-1234567890"
# str3 = "0091 9234567801"
# str4 = "91 9267384670"
# m = normallize_phones(str1)
# n = normallize_phones(str2)
# a = normallize_phones(str3)
# b = normallize_phones(str4)
# print(m)
# print(n)
# print(a)
# print(b)