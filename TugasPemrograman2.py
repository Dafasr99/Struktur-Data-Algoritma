import tkinter as tk
from tkinter import messagebox

OPERATORS = set(['+', '-', '*', '/', '(', ')', '$'])  # set of operators
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '$': 3}  # dictionary having priorities

# Function to delete the contents of the input field (Entry)
def clear_fields():
    infix_entry.delete(0, tk.END)
    postfix_label.config(text="Postfix expression: ")
    result_label.config(text="Result: ")

# Function to convert infix expression to postfix
def infix_to_postfix(expression):  # input expression
    operator = []  # initially operator empty
    output = []  # initially output empty
    str_num = ''  # empty string for number
    count = len(expression)  # based on input length

    # Loop untuk mengonversi ekspresi infix ke postfix
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
                        raise ValueError('Missing open parenthesis')
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


# Function to evaluate postfix expressions and calculate the result
def evaluate_postfix(postfix_exp):
    operand = []
    operator = {'+', '-', '*', '/', '$'}

    # Function to evaluate postfix expressions and calculate the result
    for i in postfix_exp.split():
        if i.isdigit():
            operand.append(int(i))
        elif i in operator:
            if len(operand) < 2:
                raise ValueError('Missing operand')
            num2 = operand.pop()
            num1 = operand.pop()
            if i == '+':
                operand.append(num1 + num2)
            elif i == '-':
                operand.append(num1 - num2)
            elif i == '*':
                operand.append(num1 * num2)
            elif i == '/':
                try:
                    operand.append(num1 // num2)
                except ZeroDivisionError:
                    raise ValueError('Division by zero')
                    operand.append(num1)
            elif i == '$':
                operand.append(num1 ** num2)

    if len(operand) == 1:
        return operand[0]
    else:
        raise ValueError('Missing operand')

# Functions to evaluate infix expressions, convert to postfix, and display evaluation results in the GUI
def calculate_postfix_result(): 
    try: 
        expression = infix_entry.get()
        postfix = infix_to_postfix(expression)
        postfix_str = " ".join(postfix)
        postfix_label.config(text="Postfix expression: " + postfix_str)

        result = evaluate_postfix(postfix_str)
        result_label.config(text="Result: " + str(result))

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to clear the contents of the input field and set the postfix and result labels to be empty
def input_again():
    infix_entry.delete(0, tk.END)
    postfix_label.config(text="Postfix expression: ")
    result_label.config(text="Result: ")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Postfix Expression Evaluator")
    root.geometry("400x200")
    root.configure(bg="pink")

    infix_label = tk.Label(root, text="Input Infix Expression:", bg="pink")
    infix_label.pack()

    infix_entry = tk.Entry(root)
    infix_entry.pack()

    evaluate_button = tk.Button(root, text="Evaluate Postfix", command=calculate_postfix_result)
    evaluate_button.pack()

    input_again_button = tk.Button(root, text="Input", command=input_again)
    input_again_button.pack()

    postfix_label = tk.Label(root, text="", bg="pink")
    postfix_label.pack()

    result_label = tk.Label(root, text="", bg="pink")
    result_label.pack()

    root.mainloop()