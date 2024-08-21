# Python List Methods Examples

# 1. append() - Adds an element to the end of the list
my_list = [1, 2, 3]
my_list.append(0)
print(my_list)  # Output: [1, 2, 3, 4]

# # 2. extend() - Adds multiple elements to the end of the list
# my_list.extend([5, 6])
# print("extend():", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# # 3. insert() - Inserts an element at a specified position
# my_list.insert(2, 'a')
# print("insert():", my_list)  # Output: [1, 2, 'a', 3, 4, 5, 6]

# # 4. remove() - Removes the first occurrence of an element
# my_list.remove('a')
# print("remove():", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# # 5. pop() - Removes and returns the element at the given position
# last_item = my_list.pop()
# print("pop():", my_list)  # Output: [1, 2, 3, 4, 5]
# print("popped item:", last_item)  # Output: 6

# # 6. clear() - Removes all elements from the list
# my_list.clear()
# print("clear():", my_list)  # Output: []

# # 7. index() - Returns the index of the first occurrence of an element
# my_list = [1, 2, 3, 4, 5]
# index = my_list.index(3)
# print("index():", index)  # Output: 2

# # 8. count() - Returns the number of occurrences of an element
# count = my_list.count(2)
# print("count():", count)  # Output: 1

# # 9. sort() - Sorts the list in ascending order
# my_list.sort()
# print("sort():", my_list)  # Output: [1, 2, 3, 4, 5]

# # 10. reverse() - Reverses the order of elements in the list
# my_list.reverse()
# print("reverse():", my_list)  # Output: [5, 4, 3, 2, 1]

# # 11. copy() - Returns a shallow copy of the list
# new_list = my_list.copy()
# print("copy():", new_list)  # Output: [5, 4, 3, 2, 1]
