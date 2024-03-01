# 2. Implement a stack data structure as discussed in lab and class [0.4 pts]
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

# 3. Using the stack, compute the overall result of an expression [0.8 pts]
def evaluate(expression):
    stack = Stack()
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char in ['+', '-', '*', '/']:
            if stack.is_empty():
                raise ValueError("Invalid expression")
            operand2 = stack.pop()
            if stack.is_empty():
                raise ValueError("Invalid expression")
            operand1 = stack.pop()
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero")
                result = operand1 / operand2
            stack.push(result)
        elif char == ' ':
            continue
        elif char == '(':
            stack.push(char)
        elif char == ')':
            sub_expression = ""
            while stack.peek() != '(':
                sub_expression = stack.pop() + sub_expression
            stack.pop()  # Discard the '('
            stack.push(evaluate(sub_expression))
        else:
            raise ValueError("Invalid character in expression")
    if stack.is_empty() or len(stack.items) > 1:
        raise ValueError("Invalid expression")
    return stack.pop()


# 1. Receive a string representing an expression as a command line parameter [0.3 pts]
import sys
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 calculator.py 'expression'")
    else:
        expression = sys.argv[1]
        try:
            result = evaluate(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
