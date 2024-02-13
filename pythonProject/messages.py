"""#modules
def hello():
    print("Hello! Have a nice day")
def bye():
    print("Bye! have a nice day")
"""
import vehicle

"""
#inheritance in python

class Animal:
    alive = True #class variable
    def eat(self):
        print("This animal is eating")
    def dangerous(self):
        print("This animal is dangerous")

class Lion(Animal):
    def hunts(self):
        print("This animal is good in hunting")
class Fish(Animal):
    def swims(self):
        print("This animal can swim")
class Hawk(Animal):
    def flys(self):
        print("This animal can fly")
#objects
lion = Lion()
fish = Fish()
hawk = Hawk()


print(lion.alive)
fish.eat()
hawk.dangerous()
fish.swims()
hawk.flys()

"""
"""
#MULTILEVEL INHERITANCE

class Organism:
    alive = True
class Animal(Organism):
    def eats(self):
        print("This animal eats")

class Pets(Animal):
    def tamed(self):
        print("Pets can be tamed")
class Dog(Pets):
    def guards(self):
        print("This animal can guard")

dog = Dog()
print(dog.alive)
dog.tamed()
dog.eats()
dog.guards()
"""
"""
#multiple inheritance = when a class is derived from more than one parent class

class Prey:
     def flee(self):
         print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
"""
"""
#Method  overriding 

class Animal:
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating carrots")

rabbit = Rabbit()
rabbit.eat()

#Method chaining
class Student:
    def First_name(self):
        print("My first_name is Muli")
        return self

    def Second_name(self):
        print("My second_name is Shem")
        return self

    def Course(self):
        print("Am taking Computer System Engineering")
        return  self

    def Year(self):
        print("Am a third year currently 3.2")
        return self

student = Student()
student.First_name()\
    .Second_name()\
    .Course()\
    .Year()
"""
"""
#Super() = Function used to give access to the methods of a parent class.
# Returns a temporary object of  a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):

        return self.length*self.width
class Cube(Rectangle):
    def __int__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume (self):
        return self.length * self.width * self.height
square = Square(3, 3)
cube = Cube(3, 3,)

print(square.area())
print(cube.volume())
"""
"""
#abstract class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Drive the car")
class Motorcycle(Vehicle):
    def go(self):
        print("You drive a motor cycle")

# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

# Passing objects as

class Car:

    color = None

class Motorcycle:
    color = None

def change_color(vehicle ,color):

    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1,"red")
change_color(car_2,"yellow")
change_color(car_3,"blue")
change_color(bike_1,"black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color )
"""
""""
#Duck typing
class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwuacking")
class Chicken:
    def walk(self):
        print("This Chicken is walking ")
    def talk(self):
        print("This Chicken is clucking")
class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
"""
"""
#WALRUS OPERATOR (:=) It assigns values to variables as part of a larger expression
print(happy:= True)
#Example

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
             break
    foods.append(food)

    #OR
foods = list()
while food := input("What do you like to take?: ") !="quit":
    foods.append(food)
"""

#Higher order function - a function that either accepts a function as an argument or returns a funtion(funtions can be treated as objects)
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)
#      or

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(3)
print(divide(45))

