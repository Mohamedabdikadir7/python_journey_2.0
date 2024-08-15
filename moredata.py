# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# 1. append() - Adds an element to the end of the list
fruits.append("date")
print("After append():", fruits)

# 2. extend() - Adds all elements of a list to another list
more_fruits = ["elderberry", "fig"]
fruits.extend(more_fruits)
print("After extend():", fruits)

# 3. insert() - Inserts an element at a specified position
fruits.insert(1, "blueberry")
print("After insert():", fruits)

# 4. remove() - Removes the first item with the specified value
fruits.remove("banana")
print("After remove():", fruits)

# 5. pop() - Removes the element at the specified position
popped_fruit = fruits.pop(2)
print(f"Popped {popped_fruit}. After pop():", fruits)

# 6. clear() - Removes all elements from the list
fruits.clear()
print("After clear():", fruits)

# Recreating the list for more examples
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 7. index() - Returns the index of the first element with the specified value
banana_index = fruits.index("banana")
print("Index of 'banana':", banana_index)

# 8. count() - Returns the number of elements with the specified value
cherry_count = fruits.count("cherry")
print("Count of 'cherry':", cherry_count)

# 9. sort() - Sorts the list
fruits.sort()
print("After sort():", fruits)

# 10. reverse() - Reverses the order of the list
fruits.reverse()
print("After reverse():", fruits)

# 11. copy() - Returns a copy of the list
fruits_copy = fruits.copy()
print("Copy of fruits:", fruits_copy)