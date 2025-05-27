# Encapsulation in Python
# In Python, encapsulation refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, 
# typically a class. It also restricts direct access to some components, which helps protect the integrity of the data and ensures proper usage.

# Encapsulation is the process of hiding the internal state of an object and requiring all interactions to be performed through an object's methods. 
# is approach:
# Provides better control over data.
# Prevents accidental modification of data.
# Promotes modular programming.

# Public Members
# Public members are accessible from anywhere, both inside and outside the class. These are the default members in Python.

class Public:
    def __init__(self):
        self.name = "John"  # Public attribute

    def display_name(self):
        print(self.name)  # Public method

obj = Public()
obj.display_name()  # Accessible
print(obj.name)  # Accessible

# Explanation:

# Public Attribute (name): This attribute is declared without any underscore prefixes. It is accessible from anywhere, both inside and outside of the class.
# Public Method (display_name): This method is also accessible from any part of the code. It directly accesses the public attribute and prints its value.
# Object (obj): An instance of Public is created, and the display_name method is called, demonstrating how public attributes and methods can be accessed directly.
# Note: The __init__ method is a constructor and runs as soon as an object of a class is instantiated.  

# Protected members
# Protected members are identified with a single underscore (_). They are meant to be accessed only within the class or its subclasses.

class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute

class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass

obj = Subclass()
obj.display_age()

# Explanation:
# Protected Attribute (_age): This attribute is prefixed with a single underscore, which by convention, suggests that it should be treated as a protected member. It's not enforced by Python but indicates that it should not be accessed outside of this class and its subclasses.
# Subclass: Here, a subclass inherits from Protected. Within this subclass, we can still access the protected attribute _age.
# Method (display_age): This method within the subclass accesses the protected attribute and prints its value. This shows that protected members can be accessed within the class and its subclasses.



# Private members
# Private members are identified with a double underscore (__) and cannot be accessed directly from outside the class. Python uses name mangling to make private members inaccessible by renaming them internally.

# Note: Python's private and protected members can be accessed outside the class through python name mangling. 

class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError

# Explanation:

# Private Attribute (__salary): This attribute is prefixed with two underscores, which makes it a private member. Python enforces privacy by name mangling, which means it renames the attribute in a way that makes it hard to access from outside the class.
# Method (salary): This public method provides the only way to access the private attribute from outside the class. It safely returns the value of __salary.
# Direct Access Attempt: Trying to access the private attribute directly (obj.__salary) will result in an AttributeError, showing that direct access is blocked. This is Python's way of enforcing encapsulation at a language level





























