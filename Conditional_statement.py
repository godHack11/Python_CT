# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# If Statement
if True:
	print('Conditional was True')

if False:
	print('Conditional was False')

language = 'Python'
if language == 'Python': 
    print('Conditional was True')	

# #Else Statement 
language = 'Python'
if language == 'Python': 
    print('Language is Python')	
else:
     print('No Match')   


language = 'Java'
if language == 'Python': 
    print('Language is Python')	
else:
     print('No Match')    

# Else Statement 
language = 'Java'

if language == 'Python': 
    print('Language is Python')	
elif language == 'Java':
    print('Language is Java')
else:    
     print('No Match')  


# And
# Or
# not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
   print('Admin Page')
else:
	print('Bad Creds')

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
   print('Admin Page')
else:
	print('Bad Creds')


user = 'Admin'
logged_in = False

if not logged_in:
   print('Please Log In')
else:
	print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(id(a))
print(id(b))


#False Values:
       # False
       # none
       # Zero of any numeric type
       # Any empty sequence. For example, '', (), [].
       # Any empty mapping. For example, {}.

condition = False 

if condition:
   print('Evaluated to True')
else:
   print('Evaluated to False')         

condition = None 

if condition:
   print('Evaluated to True')
else:
   print('Evaluated to False')   

condition = 0 

if condition:
   print('Evaluated to True')
else:
   print('Evaluated to False') 

condition = {} 

if condition:
   print('Evaluated to True')
else:
   print('Evaluated to False') 

