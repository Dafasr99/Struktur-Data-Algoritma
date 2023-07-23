OPERATORS = set(['+', '-', '*', '/', '(', ')', '$'])  # set of operators
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '$':3} # dictionary having priorities 

# CONVERT INFIX TO POSTFIX
def infix_to_postfix(expression): #input expression
    operator = [] # initially operator empty
    output = [] # initially output empty
    str_num = '' # empty string for number 
    count = len(expression) # based on input length
    infix_to_postfix.mark = 0 

    for ch in expression:
        count -= 1
        if ch not in OPERATORS: # if ch is a number
            if ch == ' ':
                continue
            else:
                str_num += ch
                if count == 0:
                    output.append(str_num) # insert string num 
                    str_num = ''

        elif ch in OPERATORS: # if ch is a operators
            if str_num != '':
                output.append(str_num)
                str_num = ''
            if ch =='(':  # else operators should be put in operator
                operator.append('(')
            elif ch==')':
                while operator and operator[-1] != '(':
                    if ('(' not in operator):
                        infix_to_postfix.mark = 1 # Check if missing open parenthesis
                    output+=operator.pop()
                if '(' in operator:
                    operator.pop()
            elif ch =='$': # Right-associative : langsung push 
                operator.append(ch)
            else:
                # lesser priority can't be on top on higher or equal priority    
                # so pop and put in output   
                while operator and operator[-1]!='(' and PRIORITY[ch]<=PRIORITY[operator[-1]]:
                    output+=operator.pop()
                operator.append(ch)
    while operator:
        output+=operator.pop()
    return output

# EVALUATION POSTFIX
def result(post):
    operand = []
    operator = ['+', '-', '*', '/', '$']
    result.missing = 0

    for i in post:
        if(i == ' '):
            continue
        elif (i not in operator):
            operand.append(i)
        else:
            num2 = int(operand.pop())
            if (len(operand) == 0): # Handle if missing operand
                result.missing = 1 
                operand.append(num2)
            else:
                num1 = int(operand.pop())
                if (i == '+'):
                    operand.append(num1 + num2)
                elif (i == '-'):
                    operand.append(num1 - num2)
                elif (i == '*'):
                    operand.append(num1 * num2)
                elif (i == '/'):
                    try:
                        operand.append(num1 // num2)
                    except ZeroDivisionError as post: # Handle if Division by zero
                        operand.append(num1)
                        print('\nError Messages: [Division by zero]')
                elif (i == '$'):
                    operand.append(num1 ** num2)

def main():
    expression = input('Input Infix Expression: ') # Ask user to input Infix Expression
    print('Postfix expression: ', end='')
    for i in infix_to_postfix(expression):
        print(i, end=' ')
    if (infix_to_postfix.mark == 1):
        print('\nError Messages: [Missing open paranthesis]') # Handle if missing open paranthesis

    # Postfix evaluation
    postfix = infix_to_postfix(expression)
    result(postfix)
    if (result.missing == 1): 
        print('\n[Missing operand]')

if __name__== '__main__' :
    main()
