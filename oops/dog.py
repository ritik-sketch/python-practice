'''
class Dog:
    species = "Canis familiaris"

def __init__(self, name, age):
    self.name = name
    self.age = age
'''
'''
from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, owner, balance):
        
        self.__owner = owner
        self.__balance = balance
    
    
    def get_balance(self):
        return self.__balance
    
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

   
    @abstractmethod
    def calculate_interest(self):
        pass



class SavingAccount(BankAccount):
    def calculate_interest(self):
        
        return self.get_balance() * 0.04   
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        
        return 0


savings = SavingAccount("Ritik", 1000)
current = CurrentAccount("Rahul", 2000)

savings.deposit(500)      
savings.withdraw(200)

print("Saving balance:", savings.get_balance())
print("Saving Interest:", savings.calculate_interest())   

print("Current balance:", current.get_balance())
print("Current Interest:", current.calculate_interest())  
'''





class Person:
  def __init__(self, name, age, job ):
    self.name = name
    self.age = age
    self.job = job

p1 = Person("ritik", 25, "software developer")
p2 = Person("rohit" , 25, "data science")

print(p1.name)
print(p1.age)
print(p1.job)
print(p2.name)
print(p2.age)
print(p2.job)


class Car:
  def __init__(self, color, brand, year):
    self.color = color
    self.brand = brand
    self.year = year 

  def display_info(self):
    print(f"{self.color} {self.brand} ({self.year})")

  def update_color(self, new_color):
    self.color = new_color

  def __str__(self):
    return f"{self.color} {self.brand} ({self.year})"

myCar = Car(color="Black", brand="Audi", year=2020)

print(myCar.color)
print(myCar.brand)
print(myCar.year)
print(myCar)


