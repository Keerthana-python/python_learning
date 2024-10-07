# try:
#     num = float(input("Enter a number: "))
#     reciprocal = 1 / num
#     print("The reciprocal of num ")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")


try:
    num = float(input("Enter a number: "))
    reciprocal = 1 / num
    print("The reciprocal of {num} is {reciprocal}")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a numeric value.")