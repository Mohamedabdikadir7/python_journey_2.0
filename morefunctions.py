## will be learning more functions
def add_num(a, b):
    return a +b
result = add_num(3, 5)

def greet(name = 'alik'):
    print(f"Hello, {name}!")
greet()
def student(firstname, lastname ='Mark', standard ='Fifth'):
     print(firstname, lastname, 'studies in', standard, 'Standard')

# 1 positional argument
student('John') 

# 3 positional arguments                         
student('John', 'Gates', 'Seventh')     

# 2 positional arguments  
student('John', 'Gates')                  
student('John', 'Seventh')

def new_year_countdown(start):
    while start <= 10:
        print("Happy New Year!")
        start += 1

# Example usage:
new_year_countdown(1)
