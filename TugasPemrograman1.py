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
                    operand.append(num1)
                    print("[Division by zero]")
            elif i == '$':
                operand.append(num1 ** num2)
    
    if len(operand) == 1:
        return operand[0]
    else:
        print("[Missing operand]")
        return None

if __name__ == '__main__':
    while True:
        postfix_exp = input("Masukkan Ekspresi Postfix: ")
        result = evaluate_postfix(postfix_exp)
        if result is not None:
            print('Nilai :', result)

        choice = input("Do you want to enter another postfix expression? (y/n): ")
        if choice.lower() != 'y':
            break
