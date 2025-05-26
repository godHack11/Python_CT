# Python classes and objects
# Python is an object oriented programming language.
# Almost everything in python is an object, with its properties and methods.
# A class is like an object constructor, or a "blueprint" for creating objects.

# Creating a class
class MyClass:      # To create a class, use the keyword (class).
  x = 5
print(MyClass)  

# Create Object
# Now we can use the class named MyClass to create objects:
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

# The _init_()Function
# All classes have a function called __intt__(), ehich is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):     # The __init__() function is called automatically every time the class is being used to create a new object.
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# The __str__() Function
# The __str__() Function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string represented of the object is returned:

class Person:
  def __init__(self, name, age):     # The string representation of an object WITHOUT the __str__() function:
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):     # The string representation of an object WITH the __str__() function:
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)     


# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the opbject.
# Let us create a method in the Person class:

class Person:
  def __init__(self, name, age):     # Inserting a function that prints a greeting, and execute it on the p1 object
    self.name = name                 # the self parameter is a reference to the current instance of the class, and i's used to access variable that
    self.age = age                   # belong to the class.
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()    

# The self parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person:
  def __init__(mysillyobject, name, age):      # Use the word mysillyobject and abc instead of self
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()      


# modified Object Properties
# You can modify properties on objects like this:

#set the age of p1 to 40:
p1.age = 40
print(p1.age)


# Delete Object Properties
# You can delete properties on objects by using the del keyword:
# Delete the age prpperty from the p1 bject:

del p1.age               # It gives error
print(p1.age)

# Delete the p1 object:
del p1                   # It gives error


# The pass Statement 
#  class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:    # having an empty class definition like this, would raise an error without the pass statement
  pass




