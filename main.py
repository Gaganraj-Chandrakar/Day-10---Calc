from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

should_continue_with_new_number = True

def new_calculation():
    f_num = float(input("What's the first number?: "))

    print("+\n-\n*\n/")

    should_continue_with_ans = True

    while should_continue_with_ans == True:
        operation = input("Pick an operation: ")
        s_num = float(input("What's the next number: "))
        if operation == "+":
            ans = add(f_num, s_num)
            print(f"{f_num} {operation} {s_num} = {ans}")
        elif operation == "-":
            ans = substract(f_num, s_num)
            print(f"{f_num} {operation} {s_num} = {ans}")
        elif operation == "*":
            ans = multiply(f_num, s_num)
            print(f"{f_num} {operation} {s_num} = {ans}")
        elif operation == "/":
            ans = divide(f_num, s_num)
            print(f"{f_num} {operation} {s_num} = {ans}")
        f_num = ans

        continue_operation = input(
            f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: "
        )
        if continue_operation == 'n':
            new_calculation()

new_calculation()