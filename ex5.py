# 1. Implement such a queue based on a fixed-size Python array [0.4 pts]:
class CircularQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("enqueue None")
            return
        print("enqueue", item)
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        item = self.queue[self.front]
        print("dequeue", item)
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        item = self.queue[self.front]
        print("peek", item)
        return item


# Test the implementation
queue = CircularQueueArray(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)  # Should print "enqueue None"
queue.dequeue()
queue.dequeue()
queue.enqueue(6)
queue.dequeue()
queue.enqueue(7)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()  # Should print "dequeue None"
queue.peek()     # Should print "peek None"


# 2. Implement the queue again, this time using a circular linked list [0.4 pts]
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            new_node.next = new_node
            self.front = new_node
        else:
            new_node.next = self.front
            self.rear.next = new_node
        self.rear = new_node
        print("enqueue", item)

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        item = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        print("dequeue", item)
        return item

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        item = self.front.data
        print("peek", item)
        return item


# Test the implementation
queue = CircularQueueLinkedList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.peek()
queue.dequeue()
queue.dequeue()
queue.enqueue(4)
queue.peek()
queue.dequeue()
queue.enqueue(5)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.peek()


# 3. Generate a list of 40 operations, together with expected output, that can be used to test correctness of implementation. [0.2 pts]:
operations = [
    # Regular operations
    ("enqueue", 1),
    ("enqueue", 2),
    ("enqueue", 3),
    ("peek", None),  # Should print "peek None"
    ("dequeue", 1),
    ("enqueue", 4),
    ("peek", 2),
    ("dequeue", 2),
    ("dequeue", 3),
    ("peek", 4),
    ("enqueue", 5),
    ("enqueue", 6),
    ("enqueue", 7),
    ("enqueue", 8),
    ("enqueue", 9),
    ("enqueue", 10),
    ("enqueue", 11),
    ("enqueue", 12),
    ("enqueue", 13),
    ("enqueue", 14),
    ("enqueue", 15),
    ("enqueue", 16),
    ("enqueue", 17),
    ("enqueue", 18),
    ("enqueue", 19),
    ("enqueue", 20),
    ("enqueue", 21),  # Should print "enqueue None"
    ("dequeue", 4),
    ("dequeue", 5),
    ("dequeue", 6),
    ("dequeue", 7),
    ("dequeue", 8),
    ("dequeue", 9),
    ("dequeue", 10),
    ("dequeue", 11),
    ("dequeue", 12),
    ("dequeue", 13),
    ("dequeue", 14),
    ("dequeue", 15),
]
