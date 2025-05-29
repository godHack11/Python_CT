# PIP is a package manager for Python packages, or modules if you like.
# Note: If you have Python version 3.4 or later, PIP is included by default.

# What is a Package?
# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.

# Check if PIP is Installed
# Navigate your command line to the location of Python's script directory, and type the following:

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

# Using a Package
# Once the package is installed, it is ready to use.
# Import the "camelcase" package into your project.

import camelcase
c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"
print(c.hump(txt))
#This method capitalizes the first letter of each word.

# Find Packages
# Find more packages at https://pypi.org/.

# Remove a Package
# Use the uninstall command to remove a package:
pip uninstall camelcase

# List Packages
# Use the list command to list all the packages installed on your system:

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list


