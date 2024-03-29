import matplotlib.pyplot as plt
import random
import timeit

#Ai generation(chatgbt) used to help fix syntax of the Queue inorder to better answer the question in reguards to the 
#requirements. As well as used to help implement enqueue w/ probability 0.7, or a dequeue w/
#probability 0.3,  my group and I were stuck on how to make it work. 

class ArrayQueue:
    def __init__(self):
        # Initializing empty list  
        self.elements = []
    def enqueue(self, item):
        # Insert item   
        self.elements.insert(0, item)
    def dequeue(self):
        #  queue is empty 
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        # Remove and return the last item 
        return self.elements.pop()
    def is_empty(self):
        # True if empty, False if not
        return len(self.elements) == 0
    def size(self):
        #  number of elements 
        return len(self.elements)
    def peek(self):
        # Return the element  
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.elements[-1]

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, item):
        new_node = ListNode(item)
        # new node is head and tail
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            # add new node  
            new_node.next = self.head
            self.head = new_node
    def dequeue(self):
        # if queue is empty
        if self.is_empty():
            raise IndexError("empty queue") 
        if self.head == self.tail:
            dequeued_value = self.head.value
            self.head = self.tail = None
            return dequeued_value
        # remove the element
        current = self.head
        while current.next != self.tail:
            current = current.next
        dequeued_value = self.tail.value
        self.tail = current
        self.tail.next = None
        return dequeued_value
    def is_empty(self):
        return self.head is None
    def peek(self):
        if self.is_empty():
            raise IndexError(" empty queue")
        return self.tail.value
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

def generateRandomTasks(num_tasks=10000):
    return random.choices(['enqueue', 'dequeue'], weights=[0.7, 0.3], k=num_tasks)

# Random tasks
taskLists = [generateRandomTasks() for _ in range(100)]

def testQueuePerformance(queueClass, tasks):
    queue = queueClass()
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(random.randint(0, 100))
        elif task == 'dequeue' and not queue.is_empty():
            queue.dequeue()

# Performance
arrayQueueTimes = [timeit.timeit(lambda: testQueuePerformance(ArrayQueue, tasks), number=1) for tasks in taskLists]
linkedListQueueTimes = [timeit.timeit(lambda: testQueuePerformance(LinkedListQueue, tasks), number=1) for tasks in taskLists]

# Ploting
plt.hist(arrayQueueTimes, alpha=0.5, label='ArrayQueue', bins=20)
plt.hist(linkedListQueueTimes, alpha=0.5, label='LinkedListQueue', bins=20)
plt.xlabel('Time (s)')
plt.ylabel('Frequency')
plt.title('Performance Comparison of the twp Queue Implementations')
plt.legend()
plt.show()