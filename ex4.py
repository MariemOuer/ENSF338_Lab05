import matplotlib.pyplot as plt
import random
import timeit

class ArrayQueue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.elements = []
    def enqueue(self, item):
        # Insert an item at the head (beginning) of the list
        self.elements.insert(0, item)
    def dequeue(self):
        # Check if the queue is empty before removing an item
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        # Remove and return the last item from the list (tail of the queue)
        return self.elements.pop()
    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        return len(self.elements) == 0
    def size(self):
        # Return the number of elements in the queue
        return len(self.elements)
    def peek(self):
        # Return the element at the tail without removing it
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
        # If the queue is empty, new node becomes both head and tail
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            # Otherwise, add the new node at the head
            new_node.next = self.head
            self.head = new_node
    def dequeue(self):
        # Check if the queue is empty
        if self.is_empty():
            raise IndexError("empty queue")
        # If the queue has only one element
        if self.head == self.tail:
            dequeued_value = self.head.value
            self.head = self.tail = None
            return dequeued_value
        # Otherwise, remove the tail element
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

# Generate a list of random tasks
taskLists = [generateRandomTasks() for _ in range(100)]

def testQueuePerformance(queueClass, tasks):
    queue = queueClass()
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(random.randint(0, 100))
        elif task == 'dequeue' and not queue.is_empty():
            queue.dequeue()

# Measure performance for each queue implementation
arrayQueueTimes = [timeit.timeit(lambda: testQueuePerformance(ArrayQueue, tasks), number=1) for tasks in taskLists]
linkedListQueueTimes = [timeit.timeit(lambda: testQueuePerformance(LinkedListQueue, tasks), number=1) for tasks in taskLists]

# Plot the distributions
plt.hist(arrayQueueTimes, alpha=0.5, label='ArrayQueue', bins=20)
plt.hist(linkedListQueueTimes, alpha=0.5, label='LinkedListQueue', bins=20)
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Performance Comparison of Queue Implementations')
plt.legend()
plt.show()