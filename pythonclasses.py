'''
Everything in Python is an object.

This means is that every Python variable or piece of data has attributes and/or 
methods encapsulated within the object.

Python provides a dir() function that can be used to list an object’s members 
(attributes and methods):
'''
# nums = [1,2,3]
# print (dir(nums))
# About the methods that start&end with _ : https://rszalski.github.io/magicmethods/

#Creating a Class:

class Dog():
  # 'age=0' is how you set a default value in a class
  def __init__(self, name, age=0):
    self.name = name
    self.age = age

  def bark(self):
    print(f'{self.name} says woof!')
# next we override print()'s __str__ method to make it print the way we want it too for this class
  def __str__(self):
    return f'Dog named {self.name} is {self.age} years old'



# mocha = Dog('Mocha', 2)
# mocha.bark()
# print(mocha)

'''👀 KEY POINT: Unlike Python dictionaries that use square bracket 
notation to access/set its items values, objects instantiated by 
our own Python classes are more like JS objects in that they use 
dot notation instead.'''

class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model
        # will define running here cause we don't want anyone passing something in for it
        self.running = False
    def start(self):
       self.running = True
       print('running...')
    def stop(self):
       self.running = False
       print('stopped...')
    def __str__(self):
       return f'Vehicle is a {self.make} {self.model}'
    
# car = Vehicle('Tesla', 'Model S')
# car.start()
# print(car.running)


# SETTING UP ATTRIBUTES THAT ARE SHARED BY ALL INSTANCES OF THE CLASS:

class Dog():
    #CLASS ATTRIBUTES:
    next_id = 1
    # 'age=0' is how you set a default value in a class
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        # Gives this dog an Id
        self.id = Dog.next_id
        # Increment the ID number, so the next Dog instance has it's own ID number
        Dog.next_id += 1
    def bark(self):
        print(f'{self.name} says woof!')
    # next we override print()'s __str__ method to make it print the way we want it too for this class
    def __str__(self):
        return f'Dog {self.id} named {self.name} is {self.age} years old'
    # whatever comes after this class method decorator is accessible by the Class itself
    # not the instance
    @classmethod
    def get_total_dogs(cls):
       #'cls' represents the overall Dog class
       return cls.next_id - 1
    
zayne = Dog('Zayne', 2)
mocha = Dog('Mocha', 2)
thugga = Dog('Thugga', 3)
print(Dog.get_total_dogs())


# PYTHON INHERITANCE: SUPERCLASS & SUBCLASS
# https://www.programiz.com/python-programming/inheritance