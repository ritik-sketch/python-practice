
#Q1. Write a program to take two variables of different data types and print:
#their values

#their data types
#👉 Interview focus: type() understanding

"""
a = 10
b = "Hello Ritik"
print(a)
print(b)
print(type(a))
print(type(b))
"""


"""
2. Type Conversion

Q2. Write a program where:

one variable is a string "100"

another variable is integer 50
Convert the string into integer and print their sum.

👉 Interview focus: int(), str(), real-world data handling
"""
"""
str = "100"
int_num = 50
sum = int(str) + int_num
print("sum:", sum)
"""

""" 
3. Built-in Functions

Q3. Given a list of numbers, write a program to print:

maximum value

minimum value

total count of elements

👉 Built-ins: max(), min(), len()
"""

"""
number = [10,20,30,40,50]
print(max(number))
print(min(number))

"""


"""
4. String Manipulation

Q4. Write a program to:

take a string

print its length

print the first and last character

convert it to uppercase

👉 Interview favorite
"""
"""
s = "hello"
print(len(s))
print(s.upper())
print(s[0])
print(s[-1])
"""


"""
Q5. Write a program to compare two strings and print:

"Equal" if both strings are same

"Not Equal" otherwise

👉 Interview focus: string comparison using ==
"""

""" 
str = "hello"
str2 = "hello"
if str == str2:
  print("equal")
else:
  print("not equal")
"""

""" 
Write a program to check if a number:

is greater than 10

AND less than 50
Print True or False.

👉 Interview focus: and, >, <
"""

""" 
int = 30
if int > 10 and int < 50:
  print("true")
else:
  print("false") 
"""


""" 
7. Logical Operators

Q7. Write a program that checks:

age ≥ 18 OR

has voter ID
If any condition is true, print "Eligible to Vote".

👉 Real-life logic question
""" 

""" 
age = 18
if age >=18:
  print("eligible to vote")
else:
  print("not eligible to vote")
"""


""" 
8. Simple if-else

Q8. Write a program to check whether a number is:

even

or odd

👉 Most asked beginner interview question
"""
""" 
num = 6
if num %2 == 0:
  print("even ")
else:
  print("odd")
"""

'''
Write a program to check:

if a username is "admin"

print "Welcome Admin"

else print "Access Denied"

👉 Authentication logic
'''
'''
username = 'admin'
if username == 'admin':
  print('welcome admin')
else:
  print('access denied')
'''

''' 
10. Nested if-else

Q10. Write a program to check exam result:

if marks ≥ 90 → "Excellent"

else if marks ≥ 60 → "Pass"

else → "Fail"

👉 Very common interview logic

'''
'''
markes = 87 
if markes >=90:
  print("excellent")
elif markes >=60:
  print("pass")
else:
  print("fail")
'''


'''
11. List Basics

Q11. Given a list of numbers:

print the list

print its length

print the last element

👉 Core list handling
'''

'''
list = [1,3,4,5,7]
print(list )
print(len(list))
print(list[-1])
'''



'''
12. List + Condition

Q12. Write a program to:

check if a given number exists in a list

print "Found" or "Not Found"

👉 Interview focus: in operator
'''
'''
num = int(input("enter a number"))
list = [ 2 , 5, 6, 1 , 3]

if num in list:
  print("found")
else:
  print("not found ")
'''

'''
Create a tuple of 5 elements and:

print the tuple

try to change one element and observe the result

👉 Interview focus: immutability concept
'''
'''
tuple = (1,3,4,5,6)
print(tuple)
tuple[0] = 8
print(tuple)
'''





'''
14. Set for Uniqueness

Q14. Given a list with duplicate values:

convert it into a set

print only unique values

👉 Real-world data cleaning concept '''
''''
list = [1,2,3,4,5,1,2,3]
unique_set = set(list)
print(unique_set )
'''

'''
15. List vs Tuple vs Set

Q15. Write a small program that:

creates one list, one tuple, and one set

prints their type

prints their length'''
''''''
'''
list = [4,6,7]
tuple =(1,4,5)
set = {8,9,7}
print(type(list))
print(type(tuple))
print(type(set))
'''
'''
print(len(list))
print(len(tuple))
print(len(set))
''' 

'''
1. Dictionary Basics

Create a dictionary with:

name

age

city

Print the complete dictionary and each value separately.
'''
'''
dic = {"name": "ritik", "age": 25, "city": "kanpur", "state": "up", "capital": "lucknow", "country": "india", "language": "hindi"}
print(dic)
print(dic["name"])

print(dic["age"])
'''


'''
2. Access Dictionary Safely

Given a dictionary, write a program to:

access a key that exists

access a key that does NOT exist
(Observe what happens)

'''
'''
dic = {"name": "ritik", "age": 25, "city": "kanpur"}
print(dic.get("name"))
print(dic.get("country"))  
'''


'''
3. Dictionary Update

Write a program to:

create a dictionary

update the value of one key

add a new key-value pair
'''
'''
dic = {"name": "ritik", "age": 25, "city": "kanpur"}
dic["age"] = 26
dic["country"] = "india"
print(dic)
'''

'''
4. Loop Through Dictionary

Given a dictionary, use a for loop to print:

all keys

all values

both key and value together

'''
'''
dic = {"name": "ritik", "age": 25, "city": "kanpur"}
for key in dic.keys():
    print("key:", key)
    print("value:", dic[key])
'''

'''
5. Count Characters Using Dictionary

Write a program to count frequency of each character in a string using a dictionary.

👉 Very common interview question
'''
''' 
dic = {}
str = "hello world"
for char in str:
   if char in dic:
      dic[char] +=1
   else:
      dic[char] = 1
'''

'''
6. Dictionary Length

Write a program to find:

number of keys in a dictionary

check if dictionary is empty

'''
'''
dic = {"name": "ritik", "age": 25, "city": "kanpur"}
print("number of keys:", len(dic))
if len(dic) == 0:
    print("dictionary is empty")
else:
    print("dictionary is not empty")
'''

'''
7. String Slicing

Given a string:

print first 5 characters

print last 3 characters

reverse the string using slicing

'''
'''
str = "royal challengers banglore"
print(str[:5])
print(str[-3:])
print(str[::-1])
'''

'''
8. List Slicing

Given a list of numbers:

print first half

print second half

print alternate elements
'''
'''
list = [1,2,3,4,5,6,7,8,9,10]
len=len(list)
print(list[:len//2])
print(list[len//2:])
print(list[::2])
'''


'''
9. for Loop Basics

Write a program to print numbers from:

1 to 10 using for loop
'''

'''
for i in range(1,11):
  print(i)
'''


'''
10. while Loop Basics

Write a program to print numbers from:

10 to 1 using while loop
'''

'''
num = 10
while num >= 1:
   print(num)
   num -=1
'''

'''
11. Sum Using Loop

Write a program to calculate the sum of numbers from 1 to n using a loop.

'''

num = 10 




