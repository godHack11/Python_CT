li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li,) # Ascending Order
s_li = sorted(li, reverse=True) # Descending Order

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)

 

 class Employee:
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.salary

s_employees = sorted(employees, key=e_sort) # Ascending order
#s_employees = sorted(employees, key=e_sort, reverse=True) #descending order

print(s_employees)

#Attergetter operator 

class Employee:
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]


s_employees = sorted(employees, key=attrgetter('age'))
#s_employees = sorted(employees, key=e_sort, reverse=True) #descending order

print(s_employees)


#  Using Lamda 

class Employee:
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

s_employees = sorted(employees, key=lambda e: e.age)

print(s_employees)
