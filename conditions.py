# age = 18
# if(age < 17):
#     print('you are youn')
# else :
#     print('you are old')

## basic if condition syntax
age = 18
if age >= 18:
    print("You are an adult")

## if else

age = 18
if age <= 16:
    print("You are an adult")
else :
    print("you are young ")

## if-elif-else Statement

age = 18
if age < 13:
    print("You are a child")
elif age > 18:
    print("You are a teenager")
else:
    print("You are an adult")

age1 = 18
if age1 >= 18:
    if age1 >= 65:
        print("You are a senior")
    else:
        print("You are an adult")
else:
    print("You are not an adult")

## Combining Conditions with Logical Operators
age = 19
has_permit = True
if(age > 18 and has_permit ):
     print("You can drive")
else:
    print("You cannot drive")

value = "hello"
if value:
    print("Value is not empty")
else:
    print("Value is empty")


def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except:
        print("An error occurred")
divide(8,2)