class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def evaluate(expression):
    stack = Stack()
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split() 
    # add spaces to () to seperate from numbers

    for token in tokens:
        if token == '(':
            stack.push(token)
        elif token == ')':
            innerexpression = []
            # need in case there are nested functions 
            while stack.peek() != '(':
                innerexpression.insert(0, stack.pop())
            stack.pop()  # Remove '('
            result = evaluate_innerexpression(innerexpression)
            stack.push(result)
            #put result into stack to be used in next calculation 
        else:
            stack.push(token)
    # will only have final result left in stack 
    return int(stack.pop())


def evaluate_innerexpression(innerexpression):
    operator = innerexpression.pop(0) # first value is operator 
    num1 = int(innerexpression.pop(0)) # second value is first number 
    num2 = int(innerexpression.pop(0)) # third value is second number 


    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ValueError("Division by zero")

    return result 


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python ex1.py '<expression>'")
        sys.exit(1)

    expression = sys.argv[1]
    result = evaluate(expression)
    print(result)