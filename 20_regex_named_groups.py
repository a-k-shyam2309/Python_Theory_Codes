# NAMED GROUPS

# import re
# text = "call me 0674-23457983"
# pat = r"(?P<STDcode>\d{4})-(?P<Numbers>\d{8})"
# m = re.search(pat,text)
# print("STD Code:" , m.group('STDcode'))
# print("Number:" , m.group('Numbers'))
# print(m.group(0))


# O/P:-
# STD Code: 0674
# Number: 23457983
# 0674-23457983


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# print()
# import re
# text = "Mail me: mymail09@gmail.com"
# pat = r"(?P<username>[\w.]+)@(?P<domain>[\w.]+)"
# m = re.search(pat , text)
# print("Username: " , m.group('username'))
# print("domain: " , m.group('domain'))


# O/P:-
# Username:  mymail09
# domain:  gmail.com
