'''
#-------python print -----------
print("hello" "ritik ")
name = "ritik"
age = 25
print(f"my name is {name },and I am {age} year old.")


py = 3.14159

print(f"the value of py - {py} is aproximatily ")


#------python string -----------

message = "hye where are you now ? i'm wating you "
print(message)

#------using concatnation ------

greeting = "namaste world"
message1 = "hye i'm ritik "
message2 = "i'm from kanpur "
quote = greeting + ',' + message1 + '.' + message2 + "!"
#print("first five char:", quote[:5])
#print("midle three char:", quote[::3])
#print("last five char:" , quote[-5::])


#-----------escape character------------

print('I\' m learning python !') #using backslash to escape a single quote
print("hello\nPython")
print("hello\tProgrammer")

#-------using backslash----------
print("This is a very long \
      string that spans \
      multiple lines.")

#------using unicode points so inclue special charcters--------

print("I \u2665 My Self")

'''






#------variable and data type in python -----------
'''
name = "ritik"
age = 25
height = 5.6

print("name:", name)
print("data type of (name):", type(name))
print("age:", age)
print("data type of (age):", type(age))
print("height:", height)
print("data type of (height):", type(height))
print("I \u2665 My Self")  
print("I \u2665 Coding")    
print("I \u2665 spend to much time with my laptop '\n' thats why im here in front of you  ")
'''

#------ convert data from one type to another -----
'''
number_str = "25"
number_int = int(number_str)
print("number as string:" , number_int)
print("number as integer:" , number_int)

x = str(100)
y = int(99)
z = float(101)

print("x =", x)
print("y =", y)
print("z =", z)
'''


#-------numeric datatype---------
'''
num_int = 67 
num_float = float(num_int)
num_str = str(num_int)
num_float = 76.46
num_int = int(num_float)
num_str =  str(num_int)
is_true = True
is_false = False
empty_value = None
'''

#num_complex = 5 + 6j

#print("integer:", num_int)
#print("float:", num_float)
#print("complex:", num_complex)


''''  #useing operator


print("sum:", num_complex + num_int )
print("difference:", num_float - num_complex)
print("multiply:", num_complex * num_float * num_int)
print("division:", num_complex // num_int)
print("module:", num_int % num_float)
print("exponetiaion:", num_complex ** num_float ** num_int)

'''
#type conversion --------------------------data type !
'''
print("float to integer:", num_int)
print("float to string:", num_str)
print("integer to float:", num_float)
print("integer to string:", num_str)
print("boolean(True):", is_true)
print("boolean(False):", is_false)
print("None:", empty_value)
'''


#----------------ARRAY---------------------
my_array = [1,2,3,4,5,6,7,8,9,10]

'''
print("array:", my_array)
print("length:", len(my_array))
print("first element:", my_array[0])
print("last element:", my_array[-1])
print("slice array:", my_array[1:7])
my_array[5] = 11
print("modified array: ", my_array)
my_array.remove(3)
print("removed value 3:", my_array)
my_array.extend([12,13,14,15])
print("extended array:", my_array)
'''
'''
print("array element ")
for item in my_array:
    print(item , end=' ')
print()

length = len(my_array)
print("length:", length)

first = None 
last = None 
if length > 0:
    first = my_array[0]
    last = my_array[-1]
print("first element:", first)
print("last element:", last )


print("slice array [1:7]: ")
for i in range(1,7):
    print(my_array[i], end=' ')
print()

for i in range(length):
    if i == 5:
        my_array[i] = 11
print("modified array:", my_array)

new_array = []
for item in my_array:
    if item != 3:
        new_array.append(item)
my_array = new_array
print("removed value 3:", my_array)

to_add = [12,13,14,15]
for item in to_add:
    my_array.append(item)
print("extended array:", my_array)
'''

#-------------string-------------------
'''
message = "hello ritik"

print(message)

def greet_user(name):
    return "hii," + name + '!'
message = greet_user("Python")
'''

#--------IMPORT MODULE ------------
'''
try:
   from  math_operations import add , substract , devide, multiply
except Exception:
    # Fallback implementation if external module is not available
    class math_operations:
        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def substract(a, b):
            # keep the original misspelled name for compatibility
            return a - b

        @staticmethod
        def subtract(a, b):
            return a - b

        @staticmethod
        def multiply(a, b):
            return a * b

        @staticmethod
        def divide(a, b):
            if b == 0:
                raise ZeroDivisionError("division by zero")
            return a / b

result = math_operations.add(5, 3)
print("addition result:", result)

result = math_operations.substract(5, 3)
print("subtraction result:", result)

result = math_operations.multiply(5, 3)
print("multiplication result:", result)

result = math_operations.divide(5, 3)
print("division result:", result)

'''

#---------variable-------------#
#globle & local 

'''
def modify_global():
  
    global_var = 20


    print("inside fun: globle_var=", global_var)
modify_global()

global_var = 10
print("outside fun: global_var=", global_var)
'''


#-------flow control-------------

'''
x= 10

if x>20:
    print("x is greater than 5")
elif x>5:
    print("x is greater than 5 but not greater than 20")
else:
    print("statement false")


for i in range(20):
    print(i)
'''

#--------if statement else statement elif statemnt -------------

'''
x = 15
#if x > 10:
if x > 10 :
    print("x is positive number")

else:
    print("x is not positive ")

numbers = [1,2,3,4,5]
for num in numbers:
   if num == 6:
      print("number found")
      break
else:
    print("number not found!,")
'''

#--------nasted if else --------------
'''
x = 10 
y = 20


if  x>y:
    print("x is greater than y ")
else:
    if x<y:
        print("x is less than y ")
    else:
        print("x is equal to y ")

num = -10 

if num>0:
    print("positive")
else:
    if num < 0:
        print("negative")
    else:
        print("zero")
        '''

#------TRUTHY AND FALSY VALUES------------------
'''
x = 10 
y = 20


if  x>y:
    print("value is truthy ")
else:
    
    print("value is falsy ")
'''
'''
string = "hello"

if string:
    print("string is truthy")
else:
    print("string is falsy")

my_list = [1,2,3,4,5]

if my_list:
   print("truthy")
   '''

#-----------while loop------------

'''
count = 0 

while count < 5:
    print("count:", count)
    count +=1

num = 1
while True:
    print(num)
    num  += 1
    if num > 5:
        break
        '''


#----------for loop -----------
'''
for num in range(5):
    print(num)

books = ["math", "bio",'chemistry']
for index ,book in enumerate(books):
    print(f"index: {index}, book: {books}")
'''
'''
for i in range (1,6):
    for j in range(1,11):
        print(i * j, end="\t")
    print()
    '''


#------------list ------------------------

'''
books = ["math", "bio",'chemistry']
for index ,book in enumerate(books):
    print(f"index: {index}, book: {books}")
books.append("english")
print(books)
print(books[0])
print(books[2])
print(books[-1])  #python support negative indexing 
print(books[1])
'''

'''

cricket = [ "bat", "ball", "gloves", "stump" , "helmet", "sunscreen", "water", "energy drink"]
try:
   for crick in cricket :
      print(crick)
except Exception as e:
   print("Error in loop:", e)
print(cricket[1:4])
print(cricket[:2])
print(cricket[2:])
print(cricket[:])
print(cricket[::2])
cricket_len = len(cricket)
print(cricket_len)
try:
   print(slice_cricket = cricket[1:4])
except Exception as e:
   print("Error in slice:", e)
print(slice(cricket))
'''

#-------------------tuple------------
'''
my_tuple = (1,2,3,4,5)
print("Tuple:", my_tuple)

mixed_tuple = ('apple',10, True, 3.14)
print("mixed tuple:", mixed_tuple)

print("first element:", mixed_tuple[0])
print("last element:", mixed_tuple[-1])

subset = my_tuple[2:4]
print("Subset:", subset)

'\n'
#accesss tuple
her_tuple= ("gussa ", "bahas", "ignore","itsok")

print("f_element:", her_tuple[0]) 
'\n'
print('s_element:', her_tuple[1])
'\n'
print('l_element:', her_tuple[-1])
print("lekin fir bhi achhi lgti hai \u2665  ")

'''

'''
my_tuple = (1,2,3,4,5,3,2,8)

index_of_three = my_tuple.index(3)
print('index of 3:', index_of_three)

index_of_two = my_tuple.index(2)
print('index of 2:', index_of_two)

tuple_len = len(my_tuple)
print("len of the tuple:", tuple_len)
'''

#-------------SET---------------


my_set = {1,2,3,4,5}
print("set:", my_set)

mixed_set = {'a',10 , 1.98, True}
print("mixed set:", mixed_set)

