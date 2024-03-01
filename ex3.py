#Ai used for generation used (chatgbt) - it explained how to implement a stack and corected our original code
#3.1
class EasyStack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.elements = []

    def put(self, item):
        # Add an item to the end of the list (top of the stack)
        self.elements.append(item)

    def get(self):
        # Check if the stack is empty before removing an item
        if not self.elements:
            raise IndexError("No elements available for removal")
        # Remove and return the last item from the list (top of the stack)
        return self.elements.pop()


#3.2 
class Node:
    def __init__(self, value):
        # Each node has a value and a pointer to the next node
        self.value = value
        self.next = None

class LinkedStack:
    def __init__(self):
        # The first node in the stack is initially None (empty stack)
        self.first = None

    def put(self, value):
        # Create a new node and add it to the beginning of the stack
        node = Node(value)
        node.next = self.first
        self.first = node

    def get(self):
        # Check if the stack is empty before removing an item
        if self.first is None:
            raise IndexError("No elements available for removal")
        # Remove the first node from the stack and return its value
        value = self.first.value
        self.first = self.first.next
        return value
