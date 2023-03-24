#his program defines a tuple called my_tuple and demonstrates all 
#the different operations that can be performed on tuples in Python,
# including indexing, slicing, concatenation, repetition, length, membership, and unpacking.

# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Indexing
print("Indexing:")
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 4

# Slicing
print("\nSlicing:")
print(my_tuple[1:4])  # Output: (2, 3, 4)
print(my_tuple[:3])  # Output: (1, 2, 3)
print(my_tuple[3:])  # Output: (4, 5)
print(my_tuple[:])  # Output: (1, 2, 3, 4, 5)

# Concatenation
print("\nConcatenation:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
print("\nRepetition:")
my_tuple = (1, 2, 3)
print(my_tuple * 3)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Length
print("\nLength:")
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # Output: 5

# Membership
print("\nMembership:")
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)  # Output: True
print(6 in my_tuple)  # Output: False

# Unpacking
print("\nUnpacking:")
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3