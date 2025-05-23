# Using a Module
def greeting(name):
    print(f"Hello, {name}!")




# Variable in Module

person1 = {
	"name": "John",
	"age": 36,
	"country": "Norway"
}    


# Re-naming a Module

# Built-in Modules

import platform

x = platform.system()
print(x)

# Using the dir() Function

import platform      # The dir() function can be used on all modules also the ones you create yourself.

x = dir(platform)
print(x)
