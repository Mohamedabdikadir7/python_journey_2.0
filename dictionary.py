''' Python dictionaries'''
# A dictionary is a collection of key-value pairs. 
# It is an unordered collection of items.
'''Create Python dictionary'''

person = {'name': 'John', 'age': 30, 'city': 'New York'}
# print(person)

'''Get the value of a specified key'''
# print(person['name'])

'''OR'''
# print(person.get('name'))

'''Get items of the dictionary'''
# print(person.items())

'''Get all keys of the dictionary'''
# print(person.keys())

'''Get all values of the dictionary'''
print(person.values())

'''Create a copy of the dictionary'''
person_copy = person.copy()
# print(f'Original dictionary: {person}')
# print(f'Dictionary copy: {person_copy}')

'''Update dictionary items'''
# person.update({'age': 31, 'country': 'USA'})
# print(person)

'''Clear the dictionary'''
person.clear()
print(person)