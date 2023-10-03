def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


result = 0
is_new_calc = True
first_number = 0
while True:
    if is_new_calc:
        first_number = float(input("What's the first number?: "))
        print('+\n-\n*\n/')
        operation = input('Pick an operation: ')
        second_number = float(input("What's the next number?: "))
    else:
        operation = input('Pick an operation: ')
        second_number = float(input("What's the next number?: "))

    operations = {
        '+': add(first_number, second_number),
        '-': subtract(first_number, second_number),
        '*': multiply(first_number, second_number),
        '/': divide(first_number, second_number)
    }

    result = operations[operation]
    print(f"{first_number} {operation} {second_number} = {result}")

    confirmation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if confirmation == 'y':
        first_number = result
        is_new_calc = False
    else:
        is_new_calc = True
