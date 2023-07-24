# Function to get a valid postfix expression from the user.
def get_postfix_expression():
    while True:
        postfix_exp = input("Masukkan Ekspresi Postfix: ")
        # Check if the input is a valid postfix expression
        try:
            tokens = postfix_exp.split()
            for token in tokens:
                if not token.isdigit() and token not in {'+', '-', '*', '/', '$'}:
                    raise ValueError("Invalid input. Please enter a valid postfix expression.")
            return postfix_exp
        except ValueError as e:
            print(e)

# Function to evaluate a given postfix expression and return the result along with any error messages.
def evaluate_postfix(postfix_exp):
    operand = []
    operator = {'+', '-', '*', '/', '$'}
    error_messages = []

    # Loop to evaluate the postfix expression
    for i in postfix_exp.split():
        if i.isdigit():
            operand.append(int(i))
            
        # Check if the operator is valid
        elif i in operator:
            if len(operand) < 2:
                error_messages.append("Missing operand")
                return operand[0], error_messages
            num2 = operand.pop()
            num1 = operand.pop()
            if i == '+':
                operand.append(num1 + num2)
            elif i == '-':
                operand.append(num1 - num2)
            elif i == '*':
                operand.append(num1 * num2)
            elif i == '/':
                if num2 == 0:
                    error_messages.append("Division by zero")
                    return num1, error_messages, 
                else:
                    operand.append(num1 // num2)
            elif i == '$':
                operand.append(num1 ** num2)

    # Check if the result is valid
    if len(operand) == 1:
        return operand[0], error_messages
    else:
        error_messages.append("Missing operand")
        return None, error_messages
    
# Main program
if __name__ == '__main__':
    continue_program = True

    # Loop to get postfix expressions from the user and evaluate them
    while continue_program:
        postfix_exp = get_postfix_expression()
        result, error_messages = evaluate_postfix(postfix_exp)
        print("Nilai: ".ljust(26), result)
        print("Error Messages: ".ljust(26), error_messages)

        # Loop to ask the user if they want to enter another postfix expression
        valid_choice = False
        while not valid_choice:
            try:
                choice = input("Do you want to enter another postfix expression? (y/n): ")
                if choice.lower() == 'y':
                    valid_choice = True
                elif choice.lower() == 'n':
                    valid_choice = True
                    continue_program = False
                else:
                    raise ValueError("Invalid input. Please enter 'y' or 'n'.")
            except ValueError as e:
                print(e)
