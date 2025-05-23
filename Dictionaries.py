student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['age'])   


#If we wnat to print different key which is not in the list then we use .get
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '777-7777'
student['name'] = 'Jane' #We can update values like this 

#print(student.get('phone', 'Not Found'))   
print(student)

#If want to update values all in oneshot then we have to use .update 
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student.update({'name': 'Jane', 'age': 26, 'phone': '777-7777'})
print(student)

# If we want to delete Any specific key 
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
del student['age'] 
#age = student.pop('age') # We can also use pop function
print(student)
#print(age)

#If we want to see how many keys and values 
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
for key, value in student.items():
	print(key, value)
