import re
def match_word(str):
    pat = r'c[aeiou][^aeiou]$'
    if (re.fullmatch(pat,str)):
        return True
    else:
        return False
    
print(match_word("cat"))
print(match_word("bat"))
print(match_word("caa"))
print(match_word("cab"))