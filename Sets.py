# Lists
# Lists are Mutable that can be changed after creation.
# Functions for printing any specific courses
 courses = ['History', 'Math', 'Physics', 'CompSci']
 print(courses)
 print(courses[2])   # If we want to print any of the specific course then we have to print like this 
 print(courses[-1])  # And we also use negative indexes too 
 print(courses[0:2]) # Here we print two indexes this is cslled slicing in python

# Here are some list methods

# Functions for adding courses in the list
 courses = ['History', 'Math', 'Physics', 'CompSci']  
 courses.append('Art')                                # If we want to add any item to our list then we have to use append function 
 courses.insert(0, 'Art')                             # If we want to add 'Art' any specific place in list the we have to use insert function
 print(courses)

# Functions for removing some values from lists
 courses = ['History', 'Math', 'Physics', 'CompSci'] 
 courses.remove('Math')
 courses.pop()
 print(courses)

# Finction for reverse the list items
 courses = ['History', 'Math', 'Physics', 'CompSci'] 
 courses.reverse()
 print(courses)

# Function for sorting the list
 courses = ['History', 'Math', 'Physics', 'CompSci'] 
 courses.sort()
 print(courses)

 nums = [1,5,2,4,3]
 nums.sort()
 print(nums)

 courses = ['History', 'Math', 'Physics', 'CompSci'] 
 courses.sort(reverse=True)
 print(courses)

# Functions for printing Min and Max values from the list
 nums = [1,5,2,4,3]
 print(min(nums))

 nums = [1,5,2,4,3]
 print(max(nums))

# Functions f0r printing sum of all numbers
 nums = [1,5,2,4,3]
 print(sum(nums))

# Function for finding the certain value of index
 courses = ['History', 'Math', 'Physics', 'CompSci'] 
 print(courses.index('CompSci'))
# If we want to check any specific item in the list simply as True or False
 print('Art' in courses)
 print('Math' in courses)

# Looping values 
 courses = ['History', 'Math', 'Physics', 'CompSci'] 
 for item in courses:
     print(item)

 courses = ['History', 'Math', 'Physics', 'CompSci'] #To get both the index and the value when looping through a list we use enumerate function
 for index, item in enumerate(courses):
     print(index, item)

 courses = ['History', 'Math', 'Physics', 'CompSci'] #We can also sytart from 1
 for index, item in enumerate(courses, start=1):
     print(index, item)

 courses = ['History', 'Math', 'Physics', 'CompSci'] #Join all course names in the list with ' - ' and store as a single string
 courses_str = ' - '.join(courses)
 print(courses_str)

 courses = ['History', 'Math', 'Physics', 'CompSci'] #Split the string back into a list using ' - ' as the separator
 new_list = courses_str.split(' - ')
 print(new_list)


# Tuples
# Tuples are Immutable that cannot be changed after creation.
# Mutable
 list_1 = ['History', 'Math', 'Physics', 'CompSci']
 list_2 =  list_1

 print(list_1)
 print(list_2)

 list_1[0] = 'Art'

 print(list_1)
 print(list_2)


# Immutable
 tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
 tuple_2 = tuple_1

 print(tuple_1)
 print(tuple_2)

 tuple_1[0] = 'Art'

 print(tuple_1)
 print(tuple_2)

# Sets
 cs_courses = ['History', 'Math', 'Physics', 'CompSci'] 
 print(cs_courses)


 cs_courses = ['History', 'Math', 'Physics', 'CompSci'] # Converting lists to sets to use the union() method
 art_courses = ['History', 'Math', 'Art', 'Design']

 cs_set = set(cs_courses)
 art_set = set(art_courses)

 all_courses = cs_set.union(art_set)

 print(all_courses)


#Empty Lists
empty_list = []
empty_list = list[]

#Empty Tuples
empty_list = []
empty_list = tuple[]

#Empty Sets
empty_list = []
empty_list = list[]






















