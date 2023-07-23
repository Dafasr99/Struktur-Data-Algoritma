def evaluate_postfix(postfix_exp):
    operand = []
    operator = {'+', '-', '*', '/', '$'}

    for i in postfix_exp.split():
        if i.isdigit():
            operand.append(int(i))
        elif i in operator:
            if len(operand) < 2:
                print("[Missing operand]")
                return None
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
                    print("[Division by zero]")
                    operand.append(num1)
            elif i == '$':
                operand.append(num1 ** num2)
    
    if len(operand) == 1:
        return operand[0]
    else:
        print("[Missing operand]")
        return None

if __name__ == '__main__':
    postfix_exp = input("Masukkan Ekspresi Postfix: ")
    result = evaluate_postfix(postfix_exp)
    if result is not None:
        print('Result:', result)
