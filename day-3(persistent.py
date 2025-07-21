'''
 
# Create a function to get 5 subject mark from the user
# Create a function to find the total of all marks
# Display all the marks and total
# Function to display the grade based on the total
# Function to display the student based on the grade order (like A ,B ,C)
 '''
'''def greet():
    print("Hello,welcome!")
greet()

def greet(name):
    print("Hello",name)
greet("Alice")

def add(a,b):
    return a+b
result=add(5,2)
print("sum is",result)


#default parameter value
def greet(name="guest"):
    print("Hello",name)
greet()
greet("Bob")

def get_details():
    name="Alice"
    age=23
    return name,age
n,a=get_details()
print("Name:",n,"Age:",a)

def add_all(*numbers):
    return sum(numbers)
print(add_all(1,2,3,4,5))

def info(**details):
    for key,value in details.items():
        print(key,":",value)
info(name="Alice",age=25,city="New york")

numbers=[10,20,30,40]
print(numbers)
print(numbers[0])
print(numbers[-1])
numbers[1]=25
print(numbers)

numbers.append(50)
numbers.insert(1,15)
numbers.remove(25)
numbers.pop()
del numbers[0]
for num in numbers:
    print(num)

import array
arr=array.array('i',[1,2,3,4])
print(arr[2])
arr.append(5)
arr.append(2)
arr.remove(3)
print(arr.tolist())

s1="Hello,Good morning"
s2=lambda func:func.upper()
print(s2(s1))

print(S2(5))
print(S2(-3))
print(n(0))

sq=lambda x:x**2
print(sq(3))

def sqdef(x):
    return x**2
print(sqdef(3))

li=[lambda arg=x:arg*10 for x in range(1,5)]
for i in li:
    print(i())

check=lambda x:"Even" if x%2==0 else "odd"
print(check(4))
print(check(7))

calc=lambda x,y:(x+y,x*y)
res=calc(3,4)
print(res)

n=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0,n)
print(list(even))

a=[1,2,3,4]
b=map(lambda x:x*2,a)
print(list(b))

from functools import reduce
a=[1,2,3,4]
b=reduce(lambda x,y:x*y,a)
print(b)
a="Revature"
b=22
msg="My name is {0} and I am {1} years old.".format(a,b)
print(msg)

a="python"
print("This article is written in {}.".format(a))

print("Hi! My name is {} and I am {} years old.".format("user",19))

name='om'
age=22
print(f"Hello,My name is {name} and age is {age}")

import inspect
def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper
@decorator
def greet():
    print("Hello,world!")
greet()
print(inspect.signature(decorator))

class Dog:
    sound="bark"
dog1=Dog()
print(dog1.sound)

class Dog:
    species="Canine"
    def __init__(self,name="sai",age=22):
        self.name=name
        self.age=age
dog1=Dog()
dog2=Dog("Buddy",3)
print(dog1.name)
print(dog1.age)
print(dog2.species)
print(dog2.name)
print(dog2.age)

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old."

dog1=Dog("Buddy",3)
dog2=Dog("Charlie",5)
print(dog1.species)
print(dog1.name)
print(dog2.name)

class Animal:
    def __init__(self,name):
        self.name=name
    def species(self):
        return "Hello"
class Dog(Animal):
    def sound(Self):
        return "woof!"
a=Animal("Generic Animal")
d=Dog("Buddy")
print(a.name)
print(d.name)
print(d.sound())
#print(a.sound())
print(a.species())
print(d.sound())
print(d.species())

class color:
    def __init__(self):
        self.name='Green'
        self.lg=self.Lightgreen()
    def show(self):
        print('Name:',self.name)
    class Lightgreen:
        def __init__(self):
            self.name='Light Green'
            self.code='024avc'
        def display(self):
            print('Name:',self.name)
            print('code:',self.code)
outer=color()
outer.show()
g=outer.lg
g.display()

class parent():
    def show(self):
        print("Inside parent")
class child(parent):
    def show(self):
        super().show()
        print("Inside child")
obj=child()
obj.show()
obj1=parent()
obj1.show()

class public:
    def __init__(self):
        self.name="John"

print(len("Hello"))
print(len([1,2,3]))
print(max(1,3,2))
print(max("a","b","c"))
def add(a,b):
    return a+b
print(add(3,4))
print(add("Hello,","world!"))
print(add([1,2],[3,4]))
class shape:
    def area(self):
        return "undefined"
class Rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
shapes=[Rectangle(2,3),circle(5)]
for shape in shapes:
    print(f"Area:{shape.area()}")

import json
x1={
    "name":"xyz",
    "age":35}
y=json.dumps(x1)
z=json.loads(y)
print(y)
print(z)
print(z["name"])
print(z["age"])'''

import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename='',
    filemode='a',
    format='%(name)s - %(levelname)s-%(message)s'
    )
logging.debug('Hello,Debug!')
logging.info('Hello,Info!')
logging.warning('Hello,warning!')
logging.error('Hello,Error!')
logging.critical('Hello,critical!')

        
        
    








    



