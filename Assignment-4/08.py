import re
text = "10-12-2025"
pat = r'(\d{2})-(\d{2})-(\d{4})'
m = re.search(pat,text)
if m :
    print("Whole: " , m.group(0))
    print("Day: ", m.group(1))
    print("Month: ", m.group(2))
    print("Year: ", m.group(3))
    print("Span: " , m.span())
    print("Last Index: " , m.lastindex)