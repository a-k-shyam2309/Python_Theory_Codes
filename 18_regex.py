# MATCH OBJECT #


import re
pat = r'(a+)(b+)(c+)'
text = 'abbcccee'
m = re.match(pat,text)
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))


# O/P:-
# <re.Match object; span=(0, 6), match='abbccc'>
# abbccc
# a
# bb
# ccc

# (group (0))-> returns the entire text that was matched by the regular expression.
# (group (n))-> starting with 1 returns the matched group in which a group is deliminated by ().



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


print("\n")
import re 
text = "call me 0674-23753291"
pat = r'(\d{4})-(\d{8})'
m = re.search(pat,text)   # Here search is used instead of match as match will start matching from the beginning but in search it will search in the entire text.
print(m.group(0))
print(m.group(1))
print(m.group(2))


# O/P:-
# 0674-23753291
# 0674
# 23753291
