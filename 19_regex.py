# last index - another attrubute of match object.
# It is an integer containing the number of the last group found during match.

# import re
# pat = r'(a+)(b+)(c+)'
# m = re.match(pat , 'abbcccee')
# for i in range (m.lastindex+1):
#     print(i,"-",m.group(i))
    
    

# O/P:-
# 0 - abbccc
# 1 - a
# 2 - bb
# 3 - ccc


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# import re
# pat = r'(a+)(b+)(c+)(e+)'
# m = re.match(pat , 'abbcccee')
# for i in range (m.lastindex+1):
#     print(i,"-",m.group(i))
    


# O/P:-
# 0 - abbccc
# 1 - a
# 2 - bb
# 3 - ccc
# 4 - ee



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# .start(i) - Starting idx of ith grp
# .end(i) - Ending idx + 1 of ith grp 
# i=0 or None it consider the whole matching string

# import re
# pat = r'(a+)(b+)(c+)(e+)'
# m = re.match(pat , 'abbcccee')
# print(m)
# print(m.start())
# print(m.end())
# print(m.start(0))
# print(m.end(1))


# <re.Match object; span=(0, 8), match='abbcccee'>
# 0
# 8
# 0
# 1
