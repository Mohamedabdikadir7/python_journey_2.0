class Employee:
    def __init__(self, name, age, salary, employee_id):
        self.name = name
        self.age = age
        self.salary = salary
        self.employee_id = employee_id

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, ID: {self.employee_id}"


class Manager(Employee):
    def __init__(self, name, age, salary, employee_id, department):
        super().__init__(name, age, salary, employee_id)
        self.department = department

    def get_details(self):
        details = super().get_details()
        return f"{details}, Department: {self.department}"


class Chairman(Employee):
    def __init__(self, name, age, salary, employee_id, job_description):
        super().__init__(name, age, salary, employee_id)
        self.job_description = job_description

    def get_details(self):
        details = super().get_details()
        return f"{details}, Job Description: {self.job_description}"


# Creating instances and printing details
employee = Employee("abdi", 23, 24000, 2344)
print(f"Employee Details: {employee.get_details()}")

manager = Manager("Abdi", 35, 50000, 5678, "HR")
print(f"Manager Details: {manager.get_details()}")

chairman = Chairman("jk", 23, 23000, 344, "group chairman")
print(f"Chairman Details: {chairman.get_details()}")


class Employee:
    def __init__(self, name, age, salary, employee_id):
        self.name = name
        self.age = age
        self.salary = salary
        self.employee_id = employee_id

# Creating an instance of Employee
total = Employee("abdi", 23, 24000, 2344)
print(total.name)
print(total.age)
print(total.salary)
print(total.employee_id)

class Manager(Employee):
    def __init__(self, name, age, salary, employee_id, department):
        # Call the constructor of the Employee class
        super().__init__(name, age, salary, employee_id)
        # Initialize the Manager-specific attribute
        self.department = department

# Creating an instance of Manager with all required arguments
man = Manager("Abdi", 35, 50000, 5678, "HR")
print(man.department)

class Chairman(Employee):
    def __init__(self, name, age, salary, employee_id , jds):
        super().__init__(name, age, salary, employee_id)
        self.jds = jds
jdss = Chairman("jk", 23 , 23000, 344 ,  "group chaiman")
   
print(jdss.jds)