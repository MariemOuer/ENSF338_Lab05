import matplotlib.pyplot as plt
import random
import timeit

#Ai generation used to help fix syntac of the Queue inorder to better answer the question in reguards to the 
#requirements. As well as used to help implement enqueue w/ probability 0.7, or a dequeue w/
#probability 0.3, we my group and I were stuck on how to make it work. 
class SimpleStack :
    def __init__(self):
        # Initialize an empty list 
        self.elements = []
        # Add item to end of list 
    def push(self, item):
        self.elements.append(item)
    # Check if stack is empty
    def pop(self):
        if self.is_empty():
            raise IndexError(" empty stack")
        # Remove and return last item
        return self.elements.pop()
    #True if empty, False if not empty 
    def is_empty(self):
        return len(self.elements) == 0
    # Return top element w/o removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.elements[-1]
    # Return the number of elements in stack
    def size(self):
        return len(self.elements)

class LinkedList_Node:
    def __init__(self, value):
        # Each LinkedList_Node has a value and a pointer to the next LinkedList_Node
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
    def push(self, value):
        new_LinkedList_Node = LinkedList_Node(value)
        # Set new LinkedList_Node's next to the current head
        new_LinkedList_Node.next = self.head
        # Update head to new LinkedList_Node
        self.head = new_LinkedList_Node

    def pop(self):
        # Check if the stack is empty
        if self.is_empty():
            raise IndexError(" empty stack")
        # Retrieve the value to return
        pop_value = self.head.value
        # Update the head to the next LinkedList_Node
        self.head = self.head.next
        return pop_value
    def is_empty(self):
        # Return True if empty, else False
        return self.head is None
    def peek(self):
        # Return value of the head element 
        if self.is_empty():
            raise IndexError(" empty stack")
        return self.head.value
    # Count elements in the stack
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Generation of random tasks
def generateRandomTasks(num_tasks=10000):
    return random.choices(['push', 'pop'], weights=[0.7, 0.3], k=num_tasks)

# Test stack performance 
def stackPerformance(stack_class, taskLists):
    for tasks in taskLists:
        stack = stack_class()
        for task in tasks:
            if task == 'push':
                stack.push(random.randint(0, 100))
            elif task == 'pop' and not stack.is_empty():
                stack.pop()


taskLists = [generateRandomTasks() for _ in range(100)]

# Measurement and collecttion of performance information
runs = 50
simpleStackTimes = []
linkedListStackTimes = []

for _ in range(runs):
    simpleStackTime = timeit.timeit(lambda: stackPerformance(SimpleStack, taskLists), number=1)
    linkedListStackTime = timeit.timeit(lambda: stackPerformance(LinkedListStack, taskLists), number=1)

    simpleStackTimes.append(simpleStackTime)
    linkedListStackTimes.append(linkedListStackTime)

# Plotting the distributions
plt.hist(simpleStackTimes, alpha=0.5, label='SimpleStack')
plt.hist(linkedListStackTimes, alpha=0.5, label='LinkedListStack')
plt.xlabel('Time (s)')
plt.ylabel('Frequency')
plt.title('Performance  Of Two Stack Implementations')
plt.legend()
plt.show()