# Creating a List
# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ['apple', 'banana', 'cherry']

# Creating a list with mixed data types
mixed_list = [1, 'hello', 3.14, True]

print(numbers)     # Output: [1, 2, 3, 4, 5]
print(fruits)      # Output: ['apple', 'banana', 'cherry']
print(mixed_list)  # Output: [1, 'hello', 3.14, True]
## Accessing Elements
fruits = ['apple', 'banana', 'cherry']
# Accessing elements in a list
print(fruits[0])   # Output: 'apple'
print(fruits[1])   # Output: 'banana'
print(fruits[2])   # Output: 'cherry'
# Modifying Elements
fruits[1] = 'blueberry'
print(fruits)
## Adding Elements
## # Appending an element to the end of the list
fruits.append('melon')
print(fruits)

# Inserting an element at a specific position
fruits.insert(1, 'banana')
print(fruits)

##Removing Elements
fruits.remove('banana')
print(fruits)

popped_friut = fruits.pop(2)
print(popped_friut)
print(fruits)