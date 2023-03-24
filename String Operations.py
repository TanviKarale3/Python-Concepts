#In this program, we start by defining a string my_string and then demonstrate various operations that can be performed on strings.
# These include:
# Define a string
my_string = "Hello, World!"

# Length of string
print("Length of string:", len(my_string))   #len(): Returns the length of the string.

# Indexing
print("First character of string:", my_string[0]) #Indexing: Accessing individual characters of the string using their index
print("Last character of string:", my_string[-1])

# Slicing
print("Substring of string from index 1 to 5:", my_string[1:6])  
print("Substring of string from index 7 to end:", my_string[7:])
print("Reverse of string:", my_string[::-1])                    #Slicing: Extracting substrings from the original string

# Concatenation
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print("Concatenated string:", concatenated_string)             #Concatenation: Combining two or more strings together

# Repetition
repeated_string = "Hello" * 3
print("Repeated string:", repeated_string)                 #Repetition: Repeating a string a certain number of times

# Replace
new_string = my_string.replace("World", "Python")           #replace(): Replacing a substring with another substring in the original string
print("Original string:", my_string)
print("Replaced string:", new_string)

# Split
split_string = "Hello, how are you today?".split()       #split(): Splitting a string into a list of substrings based on a 
print("Split string:", split_string)                     #delimiter (by default, the delimiter is whitespace)

# Join
joined_string = "-".join(split_string)               #join(): Joining a list of substrings into a single string using a specified delimite
print("Joined string:", joined_string)

# Upper and Lower
print("Uppercase string:", my_string.upper())     #upper() and lower(): Converting a string to uppercase or lowercase.
print("Lowercase string:", my_string.lower())

# Strip
strip_string = "   Hello, World!   "                   #strip(): Removing whitespace from the beginning and end of a string.
print("Stripped string:", strip_string.strip())