# What is Django?
# Django is a Python framework that makes it easier to create web sites using Python.

# Django takes care of the difficult stuff so that you can concentrate on building your web applications.

# Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features
# like login system, database connection and CRUD operations (Create Read Update Delete).

# Django is especially helpful for database driven websites.

# How does Django Work?
# Django follows the MVT design pattern (Model View Template).

# Model - The data you want to present, usually data from a database.
# View - A request handler that returns the relevant template and content - based on the request from the user.
# Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

# To install Django, you must have Python installed, and a package manager like PIP.

# PIP is included in Python from version 3.4.

# Django - Create Virtual Environment
# Virtual Environment
# It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv,
#  which is included in Python.

# The name of the virtual environment is your choice, in this tutorial we will call it myworld.

# Type the following in the command prompt, remember to navigate to where you want to create your project:
python -m venv myworld

# This will set up a virtual environment, and create a folder named "myworld" with subfolders and files, like this:

myworld
  Include
  Lib
  Scripts
  .gitignore
  pyvenv.cfg

# Django Create Project
# Once you have come up with a suitable name for your Django project, like mine: my_tennis_club, navigate to where in the file system 
# you want to store the code (in the virtual environment), I will navigate to the myworld folder, and run this command in the command 
# prompt:

django-admin startproject my_tennis_club

# Django creates a my_tennis_club folder on my computer, with this content:

my_tennis_club
    manage.py
    my_tennis_club/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
# These are all files and folders with a specific meaning, you will learn about some of them later in this tutorial, but for now, 
# it is more important to know that this is the location of your project, and that you can start building applications in it.

# Django Create App
# I will name my app members.

# Start by navigating to the selected location where you want to store the app, in my case the my_tennis_club folder, and run the 
# command below.

# If the server is still running, and you are not able to write commands, press [CTRL] [BREAK], or [CTRL] [C] to stop the server and 
# you should be back in the virtual environment.

python manage.py startapp members

# Django creates a folder named members in my project, with this content:
my_tennis_club
    manage.py
    my_tennis_club/
    members/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py

# These are all files and folders with a specific meaning. You will learn about most of them later in this tutorial.

# First, take a look at the file called views.py.

# Django Views
# Views
# Django views are Python functions that take http requests and return http response, like HTML documents.

# A web page that uses Django is full of views with different tasks and missions.

# Views are usually put in a file called views.py located on your app's folder.

# There is a views.py in your members folder that looks like this:

my_tennis_club/members/views.py:

from django.shortcuts import render

# Create your views here.
Find it and open it, and replace the content with this:

my_tennis_club/members/views.py:

from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

# Note: The name of the view does not have to be the same as the application.
# I call it members because I think it fits well in this context.

# Django URLs
# URLs
# Create a file named urls.py in the same folder as the views.py file, and type this code in it:

my_tennis_club/members/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]
# The urls.py file you just created is specific for the members application. We have to do some routing in the root directory 
# my_tennis_club as well. This may seem complicated, but for now, just follow the instructions below.

# There is a file called urls.py on the my_tennis_club folder, open that file and add the include module in the import statement, 
# and also add a path() function in the urlpatterns[] list, with arguments that will route users that comes in via 127.0.0.1:8000/.

# Then your file will look like this:

my_tennis_club/my_tennis_club/urls.py:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]
 
# If the server is not running, navigate to the /my_tennis_club folder and execute this command in the command prompt:
# python manage.py runserver

# Django Templates
# Templates
# In the Django Intro page, we learned that the result should be in HTML, and it should be created in a template, so let's do that.

# Create a templates folder inside the members folder, and create a HTML file named myfirst.html.

# The file structure should be like this:

my_tennis_club
    manage.py
    my_tennis_club/
    members/
        templates/
            myfirst.html
# Open the HTML file and insert the following:

# my_tennis_club/members/templates/myfirst.html:

<!DOCTYPE html>
<html>
<body>

<h1>Hello World!</h1>
<p>Welcome to my first Django project!</p>

</body>
</html>

# Modify the View
# Open the views.py file in the members folder, and replace its content with this:

# my_tennis_club/members/views.py:

from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
# Change Settings
# To be able to work with more complicated stuff than "Hello World!", We have to tell Django that a new app is created.

# This is done in the settings.py file in the my_tennis_club folder.

# Look up the INSTALLED_APPS[] list and add the members app like this:

my_tennis_club/my_tennis_club/settings.py:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members'
] 
# Then run this command:

python manage.py migrate

# Start the server by navigating to the /my_tennis_club folder and execute this command:

python manage.py runserver

# Django Models
# Django Models
# Up until now in this tutorial, output has been static data from Python or HTML templates.

# Now we will see how Django allows us to work with data, without having to change or upload files in the process.

# In Django, data is created in objects, called Models, and is actually tables in a database.

# Create Table (Model)
# To create a model, navigate to the models.py file in the /members/ folder.

# Open it, and add a Member table by creating a Member class, and describe the table fields in it:

my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
# The first field, firstname, is a Text field, and will contain the first name of the members.

# The second field, lastname, is also a Text field, with the member's last name.

# Both firstname and lastname is set up to have a maximum of 255 characters.

# SQLite Database
# When we created the Django project, we got an empty SQLite database.

# It was created in the my_tennis_club root folder, and has the filename db.sqlite3.

# By default, all Models created in the Django project will be created as tables in this database.

# Migrate
# Now when we have described a Model in the models.py file, we must run a command to actually create the table in the database.

# Navigate to the /my_tennis_club/ folder and run this command:

python manage.py makemigrations members

# Django creates a file describing the changes and stores the file in the /migrations/ folder:

my_tennis_club/members/migrations/0001_initial.py:

# Generated by Django 5.1.7 on 2025-03-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
    ]
# Note that Django inserts an id field for your tables, which is an auto increment number (first record gets the value 1, the second record 2 etc.), this is the default behavior of Django, you can override it by describing your own id field.

# The table is not created yet, you will have to run one more command, then Django will create and execute an SQL statement, based on the content of the new file in the /migrations/ folder.

# Run the migrate command:

python manage.py migrate

# View SQL
# As a side-note: you can view the SQL statement that were executed from the migration above. All you have to do is to run this 
# command, with the migration number:

python manage.py sqlmigrate members 0001

# Django Insert Data

# Add Records
# The Members table created in the previous chapter is empty.

# We will use the Python interpreter (Python shell) to add some members to it.

# To open a Python shell, type this command:

python manage.py shell
# Now we are in the shell, the result should be something like this:

Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb 4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
# At the bottom, after the three >>> write the following:

>>> from members.models import Member
# Hit [enter] and write this to look at the empty Member table:

>>> Member.objects.all()
# This should give you an empty QuerySet object, like this:

<QuerySet []>
# A QuerySet is a collection of data from a database.

# Read more about QuerySets in the Django QuerySet chapter.

# Add a record to the table, by executing these two lines:

>>> member = Member(firstname='Emil', lastname='Refsnes')
>>> member.save()
# Execute this command to see if the Member table got a member:

>>> Member.objects.all().values()

# Add Multiple Records
# You can add multiple records by making a list of Member objects, and execute .save() on each entry:

>>> member1 = Member(firstname='Tobias', lastname='Refsnes')
>>> member2 = Member(firstname='Linus', lastname='Refsnes')
>>> member3 = Member(firstname='Lene', lastname='Refsnes')
>>> member4 = Member(firstname='Stale', lastname='Refsnes')
>>> member5 = Member(firstname='Jane', lastname='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
...   x.save()
...
>>>
# Hit [enter] one more time at the end to exit the for loop.

# Now, if you run this command:

>>> Member.objects.all().values()


# Django Update Data

# Update Records
# To update records that are already in the database, we first have to get the record we want to update:

>>> from members.models import Member
>>> x = Member.objects.all()[4]
# x will now represent the member at index 4, which is "Stale Refsnes", but to make sure, let us see if that is correct:

>>> x.firstname
# This should give you this result:

'Stale'
# Now we can change the values of this record:

>>> x.firstname = "Stalikken"
>>> x.save()
# Execute this command to see if the Member table got updated:

>>> Member.objects.all().values()
# Hopefully, the result will look like this:

<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
{'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes'},
{'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>

# # Django Delete Data
# Delete Records
# To delete a record in a table, start by getting the record you want to delete:

>>> from members.models import Member
>>> x = Member.objects.all()[5]
# x will now represent the member at index 5, which is "Jane Doe", but to make sure, let us see if that is correct:

>>> x.firstname
# This should give you this result:

'Jane'
# Now we can delete the record:

>>> x.delete()
# The result will be:

(1, {'members.Member': 1})
# Which tells us how many items were deleted, and from which Model.

# If we look at the Member Model, we can see that 'Jane Doe' is removed from the Model:

>>> Member.objects.all().values()
<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
{'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes'}]>

# Django Update Model

# Add Fields in the Model
# To add a field to a table after it is created, open the models.py file, and make your changes:

my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField()
  joined_date = models.DateField()
# As you can see, we want to add phone and joined_date to our Member Model.

# This is a change in the Model's structure, and therefor we have to make a migration to tell Django that it has to update the database:

python manage.py makemigrations members
# Note: Make sure you are back in the virtual environment before running the command.

# The command above will result in a prompt, because we try to add fields that are not allowed to be null, to a table that already 
# contains records.

# As you can see, Django asks if we want to provide the fields with a specific value, or if we want to stop the migration and fix it 
# in the model:

python manage.py makemigrations members
You are trying to add a non-nullable field 'joined_date' to members without a default; we can't do that (the database needs something
 to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:
# I will select option 2, and open the models.py file again and allow NULL values for the two new fields:

my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
# And make the migration once again:

python manage.py makemigrations members
# Which will result in this:

Migrations for 'members':
  members\migrations\0002_member_joined_date_member_phone.py
    - Add field joined_date to member
    - Add field phone to member
# Run the migrate command:

python manage.py migrate
# Which will result in this output:

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, members, sessions
Running migrations:
  Applying members.0002_member_joined_date_member_phone... OK

(myworld) C:\Users\Your Name\myworld\my_tennis_club>


# Insert Data
# We can insert data to the two new fields with the same approach as we did in the Update Data chapter:

# First we enter the Python Shell:

python manage.py shell
# Now we are in the shell, the result should be something like this:

Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb 4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
# At the bottom, after the three >>> write the following (and hit [enter] for each line):

>>> from members.models import Member
>>> x = Member.objects.all()[0]
>>> x.phone = 5551234
>>> x.joined_date = '2022-01-05'
>>> x.save()
# This will insert a phone number and a date in the Member Model, at least for the first record, the four remaining records will 
# for now be left empty. We will deal with them later in the tutorial.

# Execute this command to see if the Member table got updated:

>>> Member.objects.all().values()
# The result should look like this:

<QuerySet [
{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes', 'phone': 5551234, 'joined_date': datetime.date(2022, 1, 5)},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}]>








