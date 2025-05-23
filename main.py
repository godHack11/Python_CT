import mymodule

mymodule.greeting("Jonathan")

	# 	We created a custom Python module called mymodule.py that contains a function named greeting.
	# 	The greeting function takes a name as input and prints a message.
	# 	In main.py, we imported the mymodule and called the greeting function using mymodule.greeting("Jonathan").
	# 	This demonstrates how to define and use a custom module in Python.


import mymodule
a = mymodule.person1["age"]
print(a)

	# 	In mymodule.py, we defined a dictionary person1 with keys like "name", "age", and "country".
	# 	In main.py, we imported mymodule and accessed the value of the "age" key using mymodule.person1["age"].
	# 	This shows how to store data in a module and access it in another file using module import.


import mymodule as mx

a = mx.person1["age"]
print(a)
