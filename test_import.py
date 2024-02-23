import random

# Define an empty list
var = []

# Print the type of the variable var
print(type(var))

# Define a list with integers and a string
var2 = [151, 251, 386, 493, 649, "009"]

# Print the list var2
print(var2)

# Append an integer to the list var2
var2.append(721)

# Print the modified list var2
print(var2)

# Print the available methods for the list var2
print(dir(var2))

# Define a list of integers
numbers_hard_coded = [0, 1, 2, 3, 4]

# Print the list numbers_hard_coded
print(numbers_hard_coded)

# Define a range of integers from 0 to 4
numbers = range(5)

# Print the range object numbers
print(numbers)

# Print the type of the variable numbers
print(type(numbers))

# Convert the range object numbers to a list
numbers = list(numbers)

# Print the list numbers
print(numbers)

# Define a list of integers from 0 to 9 using list comprehension
numbers = list(range(10))  # one liner

# Print the list numbers
print(numbers)

# Print the square of each number in the list numbers
for number in numbers:
    print(number ** 2)
    
# Generate a list of 10 random integers between 0 and 10 using list comprehension
var3 = [random.randint(0, 10) for i in range(10)]  # list comprehension # one liner

# Define an empty list
var4 = []

# Generate 12 random integers between 0 and 10 and append them to var4
for i in range(12):
    var4.append(random.randint(0, 10))

# Print the lists var3 and var4
print(var3)
print(var4)

# Print the element at index 5 in the list var4
print(var4[5])  # counting starts at 0 not 1

# Print the length of the list var4
print(len(var4))

# Print the cube of each index in the list var4
for i in range(len(var4)):
    print(i ** 3)
    
# Generate a list of lists with 3 lists, each containing 4 random integers between 0 and 10
list_of_lists = [[random.randint(0, 10) for j in range(4)] for i in range(3)]  # complex code

# Print the list of lists
print(list_of_lists)

# Print each list within the list_of_lists and its elements
for i in list_of_lists:
    print(i)
    for j in i:
        print(j)
