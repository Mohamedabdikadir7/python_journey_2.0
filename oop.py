'''Object-oriented Programming (OOP) in Python'''
## So, what is OOP?
# OOP is a programming paradigm that revolves around the concept of objects and classes.
# In OOP, we define a class that represents a real-world object, and then create 
# objects from that class. 
# Each object has its own set of attributes (data) and methods (functions)
# that operate on that data.

## Classes and Objects
# In Python, classes and objects are the core concepts of object-oriented programming. 
# A class is a blueprint for creating objects, and an object is an instance of a class.

## Class Definition
# A class is defined using the `class` keyword followed by the name of the class. The
# class definition includes the attributes and methods of the class.

# Here's an example of a simple class definition:
# class Class_name:
    # a variable(s)
    # a function(s)

# # Example 1
# class Student:
#     # Create variables to represent a student's data
#     name = "John"
#     age = 20
#     grade = "A"

# # Create object of the class
# # Syntax => object_name = class_name()
# obj = Student()

# # Use dot notation to access class variables
# print(obj.name)  # Output: John
# print(obj.age)   # Output: 20
# print(obj.grade) # Output: A

# Example 2
# class Student:
#     # Create variables to represent a student's data
#     name = "John"
#     age = 20
#     grade = "A"

#     # This is a method that prints the student's information
#     def student_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Grade: {self.grade}")


# # Create object of the class
# # Syntax => object_name = class_name()
# obj = Student()
# # Use dot notation to call the method
# obj.student_info()


class students:
    age = 30
    name = "abdi"
    salary = 30000


obj = students()
print(students.age)
print(students.name)
print(students.salary)
