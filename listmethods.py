'''my_list = [1, 2, 3, 4]
ch = int(input(Choose an operation:
1. append
2. clear
3. copy
4. count
5. extend
6. insert
7. pop
8. remove
9. reverse
10. sort
\nYour choice: ))

if ch == 1:
    my_list.append(5)
    print(my_list)
elif ch == 2:
    my_list.clear()
    print(my_list)
elif ch == 3:
    li = my_list.copy()
    print(li)
elif ch == 4:
    print(my_list.count(3))
elif ch == 5:
    my_list.extend([1, 2, 3])
    print(my_list)
elif ch == 6:
    my_list.insert(1, 2)
    print(my_list)
elif ch == 7:
    removed = my_list.pop()  # optional: show what was popped
    print(f"Popped item: {removed}")
    print(my_list)
elif ch == 8:
    my_list.remove(2)  # assumes 2 is present
    print(my_list)
elif ch == 9:
    my_list.reverse()
    print(my_list)
elif ch == 10:
    my_list.sort()
    print(my_list)
else:
    print("Invalid choice")
#tuples

my_tuple = (1, 2, 3, 4, 2)
ch = int(input(Choose an operation:
1. count
2. index
3. copy
4. length
5. convert to list
\nYour choice: ))

if ch == 1:
    val = int(input("Enter value to count: "))
    print(my_tuple.count(val))
elif ch == 2:
    val = int(input("Enter value to find index of: "))
    print(my_tuple.index(val))
elif ch == 3:
    copy_tuple = my_tuple[:]  # slicing makes a shallow copy
    print("Copied tuple:", copy_tuple)
elif ch == 4:
    print("Length of tuple:", len(my_tuple))
elif ch == 5:
    converted_list = list(my_tuple)
    print("Converted list:", converted_list)
else:
    print("Invalid choice")
my_set = {1, 2, 3, 4}
ch = int(input(Choose an operation:
1. add
2. clear
3. copy
4. discard
5. remove
6. pop
7. update
8. length
\nYour choice:))

if ch == 1:
    val = int(input("Enter value to add: "))
    my_set.add(val)
    print(my_set)

elif ch == 2:
    my_set.clear()
    print(my_set)

elif ch == 3:
    copied_set = my_set.copy()
    print("Copied set:", copied_set)

elif ch == 4:
    val = int(input("Enter value to discard: "))
    my_set.discard(val)
    print(my_set)

elif ch == 5:
    val = int(input("Enter value to remove: "))
    if val in my_set:
        my_set.remove(val)
        print(my_set)
    else:
        print(f"{val} not found in set. Cannot remove.")

elif ch == 6:
    if my_set:
        removed = my_set.pop()
        print("Popped:", removed)
        print(my_set)
    else:
        print("Set is empty. Nothing to pop.")

elif ch == 7:
    elements = input("Enter comma-separated values to add: ")
    new_values = set(map(int, elements.split(',')))
    my_set.update(new_values)
    print(my_set)

elif ch == 8:
    print("Length of set:", len(my_set))

else:
    print("Invalid choice")


name=input("enter the name")
age=int(input("enter the age"))
address=input("enter the address")
print(name,age,address)

name="Revature"
print(name[0:4])
print(name[0:3:1])
print(name[:4])
print(name[2:])
print(name[-1])
print(name[-3:-1])
print(name[::-1])
          
numbers=range(1,10,2)
print(list(numbers))

def doubler_number(num):
    doubler=2
    result=num*doubler
    print(result)
doubler_number(2)
num1=5
num2=4
print(num1+num2)
print(num1-num2)
print(num1**num2)
print(nm1*num2)
print(num1/num2)
print(num1//num2)

a=5
b=3
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a**=b
print(a)

def f():
    global a
    a="Modified globally"
    print(a)
f()
print(a)
x=10
print(x)
del x
print(x)
a=200
b=33
if b>a:
    print("b is bigger than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")

i=0
if i!=0:
    if i>0:
        print("positive")
    if i<0:
        print("Negative")
else:
    print("zero")
n=5
while n>0:
    n-=1
    if n==2:
        continue
    print(n)
print("loop ended")
n=int(input())
while n>0:
    n-=1
    if n%2==0:
        continue
    print(n)
thistuple=("apple","banana","grapes")
for i in thistuple:
    print(i)
x=[1,2]
y=[4,5]
for i in x:
    for j in y:
        print(i,j)
dic={"alice":23,
     "bob":45,
     "john":34,
     "david":67}
for i in dic.keys():
    print(i)
def f():
    global a
    a="deekshitha"
f()'''

a=5
b=4
c=3
print("a is greater") if a>b and a>c print("b is greater") print("b is greater") elif b>c else print("c is greater")
    

        


    
