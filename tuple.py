#1. tuple and it's property.
# tuple is a data structure in python used to store multiple items in a single variable. 
# It is similar to a list but it is immutable, meaning that once a tuple is created, its elements cannot be modified. 
# Tuples are defined using parentheses () and can contain elements of different data types.

#2. creation of tuple
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

#3. accessing elements of a tuple
print(tuple1[0])  # Output: 1
print(tuple1[2])  # Output: 3

#4. updating a tuple
# Since tuples are immutable, you cannot update or modify their elements directly.
# However, you can create a new tuple by concatenating existing tuples or by converting the tuple to a list,
#  modifying it, and then converting it back to a tuple.
# Example of concatenating tuples
tuple2 = (6, 7, 8)
new_tuple = tuple1 + tuple2
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

#5. slicing a tuple
print(tuple1[1:4])  # Output: (2, 3, 4)


#6. traversing a tuple
for element in tuple1:
    print(element)