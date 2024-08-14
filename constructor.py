'''Python constructor'''

# A special fxn in a class => syntax & fxnality
# It is called & executed when an object is created from the class
# Therefore, there is NO need to call the constructor
# It is written as __init__()
# It is used to initialize the attributes of the class
# Two types: non-parameterized, parameterized

# Non-parameterized constructor: no parameters
# class Student:
#     def __init__(self):
#         self.name = "John"
#         self.age = 20
#         self.grade = 1
#         print("Student object created")

# # Creating an object
# s1 = Student()

#Parameterized constructor: Takes parameters
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
        
#     def student_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Grade: {self.grade}")

# # Creating an object
# s1 = Student("John", 20, 1)
# s1.student_info()