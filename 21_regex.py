
# LEARNING ABOUT HOW TO EXTRACT ALL THE HASTAGS FROM A SINGLE SENTENCE

# import re
# text = "#iter students are good at #coding #classbunk"
# pat = r'(#\w+)'
# m = re.findall(pat , text)
# print(m)


# O/P:-
# ['#iter', '#coding', '#classbunk']


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Print the words starting with uppercase

import re
text = "how Are you Today"
pat = r'[A-Z]\w+'
m = re.findall(pat , text)
print(m)


# O\P:-
# ['Are', 'Today']
