## A list in Python is an ordered, mutable collection of elements
## they are like arrays in js 
fruits = ["apple" , "mango" ,"banana" , "cherry" , "pineapple"]

# sorting 
# fruits.sort()
# print(fruits)

# ## accesing list 
# print(fruits[0])  # Output: apple

# print(fruits[1:2])
# ## Modifying Elements:
# fruits[1] = 'blueberry'
# print(fruits)

## sorted
my_fruits = sorted(fruits)
print(fruits)



## modifying list
# . append add in the end
fruits.append('lemon')

# out put = 'apple', ['mango', 'banana', 'cherry', 'pineapple', 'lemon']

## .insert
## it adds in the beginning
fruits.insert(0 , 'berries')
print(fruits)

## Removing from Lists
## del() removes elements from a list, specified by an index or range of indices.
fruits = ["apple" , "mango" ,"banana" , "cherry" , "pineapple"]
del(fruits[2])
print(fruits)

fruits.clear()
print(fruits)