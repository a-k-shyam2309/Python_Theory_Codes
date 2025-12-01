import re
text1 = "Ab1"
text2 = "Ab12"
text3 = "de1"
text4 = "12Abc"
pat = r'([A-Z]).*(\d{1})'
a = re.search(pat , text1)
b = re.search(pat , text2)
c = re.search(pat , text3)
d = re.search(pat , text4)


if a:
    print(a.group(0))
    print(a.group(1))
    print(a.start(1))
    print("\n")
if b:
    print(b.group(0))
    print(b.group(1))
    print(b.start(1))
    print("\n")
if c:
    print(c.group(0))
    print(c.group(1))
    print(c.start(1))
    print("\n")
if d:
    print(d.group(0))
    print(d.group(1))
    print(d.start(1))
    print("\n")