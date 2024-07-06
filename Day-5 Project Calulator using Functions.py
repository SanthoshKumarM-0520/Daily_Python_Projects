"""Calculator Program with Basic Operations
This Python program utilizes functions to perform arithmetic operations
(addition, subtraction, multiplication, division) based on user input,
providing a user-friendly interface for calculations"""

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": divide
}

def calculator():
    first_num = int(input("Please enter the first number: "))
    condition = True
    while condition:
        for op in operation:
            print(op)
        action = input("Enter the operation you would like to perform: ")
        second_num = int(input("Enter the next number: "))
        operation_func = operation[action]
        result = operation_func(first_num, second_num)
        print(f"The result is {result}")
        again = input("Would you like to continue (yes / no / new): ")
        if again == "yes":
            first_num = result
        elif again == "no":
            condition = False
            print("Goodbye.")
        elif again == "new":
            calculator()

calculator()
