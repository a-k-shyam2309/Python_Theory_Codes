
#  * --> Anytimes
#  . --> Any Characters

import re
text = "Random <tag> First </tag> some text <tag> second </tag> end"
pat = r'<tag>.*</tag>'
m = re.findall(pat , text)

print(m)

for i in m:
    print(i)
