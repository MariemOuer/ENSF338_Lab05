class Stack:
    def __init__(self):
        self.items_list = []

    def push_item(self, item):
        self.items_list.append(item)

    def pop_item(self):
        if not self.is_empty():
            return self.items_list.pop()
        else:
            return None

    def peek_item(self):
        if not self.is_empty():
            return self.items_list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items_list) == 0

    def size(self):
        return len(self.items_list)


def evaluate_expression(expression):
    stack = Stack()
    tokens = tokenize(expression)

    for token in tokens:
        if token == ')':
            inner_expression = []
            while stack.peek_item() != '(':
                inner_expression.insert(0, stack.pop_item())
            stack.pop_item()  # Remove '('
            result = evaluate_inner_expression(inner_expression)
            stack.push_item(result)
        else:
            stack.push_item(token)
    return int(stack.pop_item())


def evaluate_inner_expression(inner_expression):
    operator = inner_expression.pop(0)
    result = int(inner_expression.pop(0))

    # going through the operators and operands
    while inner_expression:
        operand = int(inner_expression.pop(0))
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            if operand != 0:
                result /= operand
            else:
                raise ValueError("Division by zero")
    return result

#breaking up the expression
def tokenize(expression):
    tokens = []
    current_token = ''
    for char in expression:
        if char in '()':
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        elif char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ''
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)
    return tokens


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python ex1.py '<expression>'")
        sys.exit(1)

    expression = sys.argv[1]
    result = evaluate_expression(expression)
    print(result)
