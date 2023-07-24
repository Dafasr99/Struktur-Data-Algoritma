import tkinter as tk

OPERATORS = set(['+', '-', '*', '/', '(', ')', '$'])  # set of operators
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2,
            '$': 3}  # dictionary having priorities

# convert infix to postfix
def infix_to_postfix(expression):  # input expression
    operator = []  # initially operator empty
    output = []  # initially output empty
    str_num = ''  # empty string for number
    count = len(expression)  # based on input length
    infix_to_postfix.mark = 0  # Add a mark variable to check if missing open parenthesis

    for ch in expression:
        count -= 1
        if ch not in OPERATORS:  # if ch is a number
            if ch == ' ':
                continue
            else:
                str_num += ch
                if count == 0:
                    output.append(str_num)  # insert string num
                    str_num = ''

        elif ch in OPERATORS:  # if ch is an operator
            if str_num != '':
                output.append(str_num)
                str_num = ''
            if ch == '(':  # else operators should be put in operator
                operator.append('(')
            elif ch == ')':
                while operator and operator[-1] != '(':
                    if '(' not in operator:
                        infix_to_postfix.mark = 1  # Check if missing open parenthesis
                    output += operator.pop()
                if '(' in operator:
                    operator.pop()
            elif ch == '$':  # Right-associative: langsung push
                operator.append(ch)
            else:
                # lesser priority can't be on top on higher or equal priority
                # so pop and put in output
                while operator and operator[-1] != '(' and PRIORITY[ch] <= PRIORITY[operator[-1]]:
                    output += operator.pop()
                operator.append(ch)
    while operator:
        output += operator.pop()
    return output

# Evaluate postfix expressions and calculate the result


def result(post):
    operand = []
    operator = ['+', '-', '*', '/', '$']
    result.missing = 0
    result.error_messages = []  # Add an error_messages list to store all error messages

    for i in post:
        if i == ' ':
            continue
        elif i not in operator:
            operand.append(i)
        else:
            num2 = int(operand.pop())
            if len(operand) == 0:  # Handle if missing operand
                result.missing = 1
                operand.append(num2)
            else:
                num1 = int(operand.pop())
                if i == '+':
                    operand.append(num1 + num2)
                elif i == '-':
                    operand.append(num1 - num2)
                elif i == '*':
                    operand.append(num1 * num2)
                elif i == '/':
                    try:
                        operand.append(num1 // num2)
                    except ZeroDivisionError as e:  # Handle if Division by zero
                        operand.append(num1)
                        result.error_messages.append(
                            'Error Messages: [Division by zero]')  # Store the error message
                elif i == '$':
                    operand.append(num1 ** num2)
    return operand[-1]

# Function to calculate the result and display the result and any error messages


def on_calculate(event=None):
    expression = entry_expression.get()
    postfix = infix_to_postfix(expression)
    result_value = result(postfix)

    postfix_label.config(text="Postfix expression: " + ' '.join(postfix))
    result_label.config(text="Result: " + str(result_value))

    errors = []
    if infix_to_postfix.mark == 1:
        errors.append("Error Messages: [Missing open parenthesis]")
    if result.missing == 1:
        errors.append("Error Messages: [Missing operand]")
    # Add the division by zero error message
    errors.extend(result.error_messages)
    error_label.config(text=", ".join(errors) if errors else "", fg="red")


# Create the main window
root = tk.Tk()
root.title("Convert from Infix Expression to Postfix Expression")

# Create the expression input entry
entry_expression = tk.Entry(root, width=30)
entry_expression.pack(pady=10)
# Bind the Return key to on_calculate()
entry_expression.bind("<Return>", on_calculate)

# Create the calculate button
calculate_button = tk.Button(
    root, text="Calculate", command=on_calculate, bg="pink", fg="black", font=("Arial", 12))
calculate_button.pack()

# Create the postfix label
postfix_label = tk.Label(root, text="Postfix expression: ")
postfix_label.pack(pady=5)

# Create the result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

# Create the error label
error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=5)

# Start the GUI main loop
root.mainloop()
