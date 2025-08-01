from statistics import harmonic_mean

col = 1

if col == 1 :
    print('one')
else:
  print("not one")
  print("hey")
# --------------------------- #
# VARIABLES
# --------- #
# string
print('text')
# integer
print(2)
# float
print(3.4)
# boolean
print(True)

# IF statement
# --- #
a=7
if a<5:
    print(a)
elif a!=4:
    print(a)
else:
    print(a)
# FOR LOOP
#--------#
a=5
a=str(a)
for x in a:
    print(x)
# FUNCTIONS
def get_type(p):
    return (type(p))
result = type(a)
print(result)
# LIST, TUPLE
# create list #
x=[1,2,3,]
print(x)
# index
print(x[2])
#add
print(x.append(5))
x.append(5)
print(x)
#insert
x.insert(0,0)
print(x)
x[4]=4
print(x)
#index count
print(x.count(2))
#lenght
print(len(x))
e=[6,7,8]
x.extend(e)
print(x)
# x.revers()
# print(x)



# PYTHON DICTIONARY
# dictionary
emy={1:'jhon',2:'sam',3:'ram'}
print(emy)
print(emy[1])
print(emy.get(0))
print(emy.keys())
print(emy.values())
print({})
# add
emy[0]='jam'
print(emy)


print(emy.get(0))
d = {1:'one', 2:'two', 3:'three'}
print(d)
empty_d ={}
print(empty_d)
d['four']=4
print(d)
del d['four']
print(d)
print(d.keys())
print(d.values())
print(d[2])
print(d.get(3))
print(d.get('4'))

def numbers(a,b):
    return a+b
result = numbers(1,2)
print(result)


l=[[1,2,3,4,.5],[6,7,8,9,12],[1.2,2.3,3.3]]
def items(a):
     even=[]
     for list in a:
         for sublist in list:
            if sublist  % 2 == 0:
             even.append(sublist)
             return even
r=items(l)
print(r)

p = [5,4,7,6,8,9,10]
def even_odd(q):
    even = []
    odd =[]
    total =[]
    for x in q:
        if x % 2 == 0:
            index = q.index(x)
            even.append(index)
        else:
            index = q.index(x)
            odd.append(index)
    total.append(even)
    total.append(odd)
    return total
r = even_odd(p)
print(r)

s = [[[1]]]
# s[0][0][0]
print(s[0][0][0])

y = [5,4,7,6,8,9,10]
def even_sqaure(y):
    es = []
    o=[]
    total =[]
    for g in y:
        if g % 2 ==0:
            square = g * g
            es.append(square)
        else:
            o.append(0)
    total.append(es)
    total.append(o)
    return total[1][0]
r = even_sqaure(y)
print(r)
#-----------------------------------------------------------------------------#


#if.py
# simple if
student_with_age = 18
if student_with_age >= 18:
    print("eligible")
else:
    print("not eligible")

# multiple conditions
student_with_age = 18
if student_with_age == 18:
    print("you need to get vote")
elif student_with_age > 18:
    print("you already have vote")
else:
    print("not eligible")

# complex conditions
if ("apple" == "graphes") and (1==1):
    print("i am true")
else:
    print("i don't know who i am")

# with boolean
t = True
f = False
if t:
    print("i am true")
elif f:
    print("i am false")
else:
    print("you never reach here")

# with previous topics
given_number = 3
if given_number%2 == 0:
    print("even")
else:
    print("odd")


#---------------------------------------------------------------#
#for.py
 number_1 = 1
number_1_sqaure = 1*1
print(number_1_sqaure)

number_2 = 2
number_2_sqaure = 2*2
print(number_2_sqaure)

number_3 = 3
number_3_sqaure = 3*3
print(number_3_sqaure)

number_4 = 4
number_4_sqaure = 4*4
print(number_4_sqaure)

number_5 = 5
number_5_sqaure = 5*5
print(number_5_sqaure)

#------------------
# Simple for
for number in range(1, 6, 1):
    number_square = number * number
    print(number_square)

#--------------------
# for loop with if
# print with f string (format strings)
for number in range(1, 11, 1):
    print(f"Number from for loop is {number}")
    if number%2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
#--------------------
# Nested loop
for outer_number in range(1, 6, 1):
    for inner_number in range(100, 106, 1):
        print(outer_number*inner_number)
    print("---------------")


#----------------------------------------------------------------#
#function.py
 # return sum of the numbers
def add_numbers(a: int, b: int) -> int:
     """
     add two numbers and we get sum

     parameters:
     a(int): first number
     b(int): second number

     return:
     int: sum of two number
     """
     return a+b
result = add_numbers(9,8)
print(result)

# return subtract  the numbers
def subtract_numbers(a:float, b:float) -> float:
    """
    subtract two numbers and we will get result

    parameters:
    a(float): number one
    b(float): number two

    return:
    float: subract two numbers

    """
    return a-b
result = subtract_numbers(8.7,9.8)
print(result)

# return multiply numbers
def multiply_numbers(a: int,b:int, c: int) -> int:
    """
    multiply three numbers to get result

    parameters:
    a(int): number one
    b(int): number two
    c(int): number three

    return:
    integer: multiplication of  three number

    """
    return a * b * c
result = multiply_numbers(8,9,3)
print(result)

# return division of the numbers in numpy style
def divide_numbers(a:int, b:int) -> int:
    """
    divide the first number by second number we get result

    parameters :
    a(int): first number
    b(int): secound number

    return:
    integer: division of the numbers

    """
    return a/b
result = divide_numbers(25,5)
print(result)

#------------------------------------------------------------------------#
#list.py
# list can be used for create ,add, remove, any changes we do relating to data
# ex: for shopping prepare a list #
# to store list items use this "[]"
# list can store all type of data like string,integer,float,booleans.
# we can access list item by using index(item positions).

# create a list
item_types = ["text", 7, 6.7, True]

#get items by using index. in list index start from "0"
print(item_types[0],
      item_types[1],
      item_types[2],
      item_types[3])
print(item_types[-4])

# print list
print(item_types)

#change item in list
item_types[1] = 6
print(item_types)

#add item to list
item_types.append(False)
print(item_types)

# insert item in list
item_types.insert(1, 7)
print(item_types)


# remove item from list
item_types.remove(6)
print(item_types)

# delete everything in list
item_types.clear()
print(item_types)

# sort items in list
# asc
no = [4, 6, 5, 7, 6, 8, 9]
no.sort()
print(no)
# desc
no.sort(reverse=True)
print(no)

# use F string & if, for loop in list
for number in no:
    if number % 2 == 0:
        print("even number")
    elif number * 2 == 4:
        print(number)
    else:
        print("-")
for number in no:
    print(type(number))

# n=5
# n=6
l=[1,2,3]
print(l[0])
print(l[1])
print(l[2])
for x in range(0,3,1):
    print(l[x])


# 123 list
l=['a','b','c']
for x in l:
    print(x)
 # ----------



a = [7,8,9]
a.sort()
for x in a:
    if x % 2 == 0:
        l= a.index(x)# position 1
        square= x*x #for loop lo nuchi vachina list number
# a.insert(l, square)#[7,64,8,9]
# a[l]= square
print(a) #[7,64,8,9]˳˳

p=[6,5,9,4,2]
def sort_number(a):
    return a.sort()
result = sort_number(p)
print(p)

l=['a','b','c','d',1,2,3]#[0,1,2,3,4,5,6]
def positions(a):
    p = []
    for x in a:
        i = a.index(x)
        p.append(i)
    return p
r = positions(l)
print(r)

l=[[1,2,3,4,.5],[6,7,8,9,12],[1.2,2.3,3.3]]
def items(a):
     even=[]
     for list in a:
         for sublist in list:
            if sublist  % 2 == 0:
             even.append(sublist)
             return even
r=items(l)
print(r)


# step = list lo nuchi even number bayatiki techam anukuna
# by using for,if fuctions
# step 2 = even number lo unna numer ni square chesta
#
# step3 = a even number unna position ni
# identify chesi square peddatha

# for x in a:
#     if x%2 ==0:
#         print(x)

# size = len(a)
# # 012 index
# for x in range(0,size):
#     if x % 2!=0:
#         print(a[x])


#------------------------------------------------------------------#
#tuple.py

# tuple can be used for craete fixed item
#ex: shopping reciept
#create a tuple by using "()"
# we cannot change,add, remove items in tuple

# create a tuple
items =("text", 7, 7.7,True)

# print tuple items
print(items[0])
print(items[0:3])
print(items)

# lenght of tuple
print(f"len:{len(items)}")

# find the "type" we use for data records
print(type(items))
l=(7.5)
print(type(l))

# use count
t=(1,22,3,3,4,7,7,7,7,7,6,8,5,9,)
print(t.count(7))
print(t.index(22))

# nesting tuple
nt = ((1,2,3,4), ('a','b','c'))
print(nt[0])
print(nt[1][2])

# concatenation (combined) tuple
n=(1,2,3,4)
l=('a', 'b', 'c')
combined = n + l
print(combined)

# repetition in tuple
repeated = (n+l)*2
print(repeated)

# use f string, for,if in tuple
items =("text", 7, 7.7,True)
for data in items:
    if isinstance(data, (str,bool)):
        print(f"string:{data},boolean:{data}")
    elif isinstance(data, float):
        print(f"float:{data}")
    else:
        print(f"integer:{data}")


import the student class from class.py
from student import Student
student1 = Student("alice", 25)
print(student1.greet())


#---------------------------------------------------------------#

#dictionary.py

# dictionary contain key; value
# ex: phone number list with names
# recored in "{}"
# it can change, add, or remove items

# create dictionary
marks = {'telugu':50,
         'hindi':67,
         'english':80,
         'maths':80}
print(marks)
# empty dictionary
ed = {}
print(ed)
# print dictionary
print(marks['maths'])
print(f"maths:{marks['maths']}")
print(marks.keys())
print(marks.values())
print(marks.get('accounts'))
print(marks.get('accounts','not avaliable'))

# add data to dictionary
marks['science'] = 90
print(marks)

# delete data in dictionary
del marks['maths']
print(marks)
# for loop
for key in marks:
    print(f"{key}:{marks[key]}")
for item in marks.items():
    print(f"subject {item[0]} and marks{item[1]}")
    print(item)


#------------------------------------------------------------------#
#class.py  

# class #
class MyPhone:
    def __init__( self,name, assist):
        self.m_name = name
        self.m_assist = assist
    def ring(self):
        print("i am ringing")
nokia = MyPhone('nokia','nokia assist')
print(nokia.m_name, nokia.m_assist)
nokia.ring()

# practice:
class Contact:
    def __init__(self,id, name):
        self.id = id
        self.name = name
    def show(self):
        print(self.id,self.name)
sam = Contact(1,'sam')
print(sam.id,sam.name)
sam.show()


class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        return f" Hello ,my name is {self.name} and i am {self.age} years old."
    person1 = Person("alice",25)
    print(personl.name)
    print(person1.age)
    person1.greet()

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        def greet(self):
            return f"hello, my name is {self.name} and i am {self.age} years old."


class Contact:
    def __init__(self, name, num):
        self.name = name
        self.number = num

    @classmethod
    def contact_switch(cls, name, num):
        contact_object = Contact(name, num)
        return contact_object

    def show_contact(self):
        print(f"name is {self.name} and number is {self.number}")


sam_contact = Contact.contact_switch("sam", "1234")
print(sam_contact.name, sam_contact.number)

#---------------------------------------------------------#
#Calculator.py


from csv import excel


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, l):
        sum = self.a + self.b
        if sum == l:
            return sum
    def subtract(self):
       return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def division(self):
        try:
            div_result = self.a / self.b
            print(f"Division result is {div_result}")
            return div_result
        except Exception as e:
            print(f"Error happened in division")
            print(e)
        finally:
            print(f"Division completed")
    def addition(self):
        try:
            if self.b == 0:
                raise Exception("Error happened")
            res = self.a + self.b
            return res
        except Exception as e:
            print(f"Exception happened {e}")

a = 25
b =25
l = 50
simple_calculator = Calculator(a,b)
addition = simple_calculator.add(l)
print(addition)
q = simple_calculator.division()
add = simple_calculator.addition()


#-----------------------------------------------------#
#csv.py

import csv
file = open ("favrites.csv","r")
# do somthing with file
close(file)
import csv
with open("favorites.csv", "r") as file:
    reader =csv.DictReader(file)
    next(reader)
    for row in reader:
        favorite =row["language"]
        print(row["language"])
        




















































































