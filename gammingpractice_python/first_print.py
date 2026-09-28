'''
print("ritik chaturvedi")
print(1+2)
print(type(1+2))
print(type("4" + "5"))


list(range(20))
print(

list(range(20)))

for i in range(1,10):
  print(i)


for i in {1,50}:
  print(i)


#*
#**
#***
#****
#*****
rows = int(input("enter the row number"))
for i in range (1, rows +1):
  for j in range(0,i):
    print("*", end=" ")
  print("")


for i in range(1,11):
  if i == 7:
    break
  print(i)

help("modules")
'''
''''
import random
a = [1,2,3,4,5]
random.shuffle(a)
print(a)
'''''

sample = "ritik chaturvedi"
print(sample.split())
L= []
for i in sample.split():
  print(i.capitalize())
  L.append(i.capitalize())
print(L)
print(" ".join(L))

sample = "rcb@gmai.com"
print(sample[:sample.find("@")])








__dict__= {"name":"ritik "}
print(__dict__)

