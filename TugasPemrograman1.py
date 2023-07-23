class Evaluator:
    def __init__(self):
        self.stack = []
        self.str = ''

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def calculate(self, token, first, second):
        try:
            if token == '+':
                return second + first
            elif token == '-':
                return second - first
            elif token == '*':
                return second * first
            elif token == '/':
                try: # Handle if divided by zero
                    self.stack.append(second // first)
                except ZeroDivisionError as e:
                    print("Nilai : ", second)
                    self.str = "[Division by zero]"
                    return
            elif token == '$':
                return second ** first
        except IndexError:
            return first

    def evaluate_postfix(self, postfix_exp):
        self.stack.clear()
        for token in postfix_exp.split():
            if token.isdigit():
                self.push(int(token))
            else:
                try:
                    first = self.pop()
                    second = self.pop()
                    result = self.calculate(token, first, second)
                    self.push(result)
                except (IndexError, ValueError) as e:
                    self.str = str(e)
                    return

        result = self.pop()
        if not self.is_empty():
            self.str = "[Invalid postfix expression]"
            return
        if self.str:
            print("Error Messages:", self.str)
        else:
            print("Nilai:", result)


if __name__ == '__main__':
    postfix_exp = input("Masukkan Ekspresi Postfix: ")
    evaluator = Evaluator()
    evaluator.evaluate_postfix(postfix_exp)
