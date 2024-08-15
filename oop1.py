"""Class
Definition: A class is a blueprint or template for creating objects. It defines attributes (data) and methods (functions) that the objects created from the class will have."""

# class Employee:
#     def __init__(self, name, age, race, salary, emp_id):
#         self.name = name
#         self.age = age
#         self.race = race
#         self.salary = salary
#         self.emp_id = emp_id
# class Employee:
#     def __init__(self, name, age, race, salary, emp_id):
#         self.name = name
#         self.age = age
#         self.race = race
#         self.salary = salary
#         self.emp_id = emp_id

#     def give_raise(self, amount):
#         self.salary += amount
#         print(f"{self.name} received a raise. New salary: ${self.salary}")

# # Creating an instance of Employee
# employee3 = Employee("Alice Brown", 40, "White", 60000, "E003")

# Using the give_raise method
# employee3.give_raise(5000)  # Output: Alice Brown received a raise. New salary: $65000

# class Pen:
#     def __init__(self, color , size) :
#         self.color = color
#         self.size = size
# markerpen = Pen( "green" ,"thick")
# mpen = Pen( "yellow" ,"thin")
# print(markerpen)

class Pen:
    def __init__(self, color, size):
        self.color = color
        self.size = size

   

markerpen = Pen("green", "thick")
mpen = Pen("yellow", "thin")

print(markerpen)
print(mpen)
