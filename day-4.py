'''from collections import Counter
words=["apple","banana","orange","apple"]
count=Counter(words)
print(count)

from collections import defaultdict
d=defaultdict(int)
d['a']+=1
print(d['a'])
print(d['b'])

from collections import OrderedDict
od=OrderedDict()
od['a']=1
od['b']=2
print(od)

from collections import namedtuple
point=namedtuple("point",["x","y"])
p=point(10,20)
print(p.x,p.y)

from collections import deque
dq=deque([1,2,3])
dq.appendleft(0)
dq.append(4)
print(dq)
dq.pop()
dq.popleft()
print(dq)
from collections import ChainMap
dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
cm=ChainMap(dict1,dict2)
print(cm['b'])
print(cm['c'])
cm['b']=6
print(cm['b'])

import re
text="Hello,my phone number is 123-456-7890'
pattern=r"\d{3}-\d{3}-\d{4}"

import re
text="Hello world"
pattern=r"Hello"
match=re.match(pattern,text)
if match:
    print("Match found at beginning")
else:
    print("No match at beginning")
import re
text="123"
pattern=r"\d+"
if re.fullmatch(pattern,text):
    print("Entire string matches pattern")
text="Contact me at john@email.com or jane@example.org"
pattern=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails=re.findall(pattern,text)
print(emails)
import re
text="The date is 2023-12-25"
pattern=r"(\d{4})-(\d{2})-(\d{2})"
replacement=r"\2/\3/\1"
new_text=re.sub(pattern,replacement,text)
print(new_text)

import re
text="apple,banan;orange:grape"
pattern=r"[,;:]"
parts=re.split(pattern,text)
parts=re.split(pattern,text)
print(parts)

try:
    result=10/0
except ZeroDivisionError:
    print("cannot divide by zero!")

try:
    value=int(input("Enter a number:"))
    result=10/value
    print(result)
except ValueError:
    print("Invalid input!please enter a number.")
except ZeroDivisionError:
    print("cannot divide by zero!")
    
try:
    pass
except(ValueError,TypeError,ZeroDivisionError) as e:
    print(f"An error occured:{e}")'''

try:
    value=int(input("enter a number:"))
except ZeroDivisionError:
    print("divide by zero 
    
          




