 message =  'Hello World'
 print(message)

 message =  'Bobby\'s World' # If we want to print this message in single quotes then we have to use back slash(\)
 print(message)

 message =  "Bobby\'s World" # Here we simply use double quotes
 print(message)

 message =  """Bobby\'s World was a good  #Triple quotes allow multiline strings, and no need to escape single quotes
 cartoon in the 1990s"""
 print(message)

message =  'Hello World'  # Print the number of characters in the string
print(len(message))

message =  'Hello World'  # Print the character at index 4
print(message[4])

message =  'Hello World'  # Print characters from index 0 up to (but not including) index 5 (Its called slicing)
print(message[0:5])


# Some string methods
message =  'Hello World'      # Convert the string to lowercase
print(message.lower())        # the string in all lowercase letters
print(message.upper())        # the string in all uppercase letters
print(message.count('Hello')) # Count how many times 'Hello' appears in the string
print(message.find('l'))      # Find the index of the first occurrence of 'l'

# #Replace method
message = 'Hello World'     # This method replace the Word
new_message = message.replace('World', 'Universe')

print(new_message)


# String concatenation
greeting =  'Hello'    # Combine greeting and name using string concatenation
name = 'Michael'
message = greeting + ', ' + name
print(message)


# F String 
greeting = 'Hello'
name = 'Michael'

message = f'{greeting}, {name}. Welcome!'
print(message)



















