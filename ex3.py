import matplotlib.pyplot as plt
import random
import timeit

#Ai generation(chatgbt) used to help fix syntax of the Queue inorder to better answer the question in reguards to the 
#requirements. As well as used to help implement enqueue w/ probability 0.7, or a dequeue w/
#probability 0.3,  my group and I were stuck on how to make it work. 
class SimpleStack :
    def __init__(self):
        # Initialize list 
        self.elements = []
        # Add item 
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
    #Return top element 
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.elements[-1]
    #number of elements in stack
    def size(self):
        return len(self.elements)

class LinkedList_Node:
    def __init__(self, value):
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

# random tasks
def generateRandomTasks(num_tasks=10000):
    return random.choices(['push', 'pop'], weights=[0.7, 0.3], k=num_tasks)

# stack performance 
def stackPerformance(stack_class, taskLists):
    for tasks in taskLists:
        stack = stack_class()
        for task in tasks:
            if task == 'push':
                stack.push(random.randint(0, 100))
            elif task == 'pop' and not stack.is_empty():
                stack.pop()


taskLists = [generateRandomTasks() for _ in range(100)]

# performance 
runs = 50
simpleStackTimes = []
linkedListStackTimes = []

for _ in range(runs):
    simpleStackTime = timeit.timeit(lambda: stackPerformance(SimpleStack, taskLists), number=1)
    linkedListStackTime = timeit.timeit(lambda: stackPerformance(LinkedListStack, taskLists), number=1)

    simpleStackTimes.append(simpleStackTime)
    linkedListStackTimes.append(linkedListStackTime)

# Plotting 
plt.hist(simpleStackTimes, alpha=0.5, label='SimpleStack')
plt.hist(linkedListStackTimes, alpha=0.5, label='LinkedListStack')
plt.xlabel('Time (s)')
plt.ylabel('Frequency')
plt.title('Performance  Of Two Stack Implementations')
plt.legend()
plt.show()