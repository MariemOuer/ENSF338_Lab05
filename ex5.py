# 1. Implement such a queue based on a fixed-size Python array [0.4 pts]:
class CircularQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    # helper function
    def is_empty(self):
        return self.size == 0

    # helper function
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


# 2. Implement the queue again, this time using a circular linked list [0.4 pts]
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    # helper function
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


# 3. Generate a list of 40 operations, together with expected output, that can be used to test correctness of implementation. [0.2 pts]:
operations1 = [
    ("peek", None),      # Peek into an empty queue, expected output: "peek None"
    ("enqueue", 1),      # Enqueue 1, expected output: "enqueue 1"
    ("enqueue", 2),      # Enqueue 2, expected output: "enqueue 2"
    ("enqueue", 3),      # Enqueue 3, expected output: "enqueue 3"
    ("peek", 1),         # Peek when queue is not empty, expected output: "peek 1"
    ("dequeue", 1),      # Dequeue 1, expected output: "dequeue 1"
    ("enqueue", 4),      # Enqueue 4, expected output: "enqueue 4"
    ("peek", 2),         # Peek front element (2), expected output: "peek 2"
    ("dequeue", 2),      # Dequeue 2, expected output: "dequeue 2"
    ("dequeue", 3),      # Dequeue 3, expected output: "dequeue 3"
    ("peek", 4),         # Peek front element (4), expected output: "peek 4"
    ("enqueue", 5),      # Enqueue 5, expected output: "enqueue 5"
    ("enqueue", 6),      # Enqueue 6, expected output: "enqueue 6"
    ("enqueue", 7),      # Enqueue 7, expected output: "enqueue 7"
    ("enqueue", 8),      # Enqueue 8, expected output: "enqueue 8"
    ("enqueue", 9),      # Enqueue 9, expected output: "enqueue 9"
    ("enqueue", 10),     # Enqueue 10, expected output: "enqueue 10"
    ("enqueue", 11),     # Enqueue 11, expected output: "enqueue 11"
    ("enqueue", 12),     # Enqueue 12, expected output: "enqueue 12"
    ("enqueue", 13),     # Enqueue 13, expected output: "enqueue 13"
    ("enqueue", 14),     # Enqueue 14, expected output: "enqueue 14"
    ("enqueue", 15),     # Enqueue 15, expected output: "enqueue 15"
    ("enqueue", 16),     # Enqueue 16, expected output: "enqueue 16"
    ("enqueue", 17),     # Enqueue 17, expected output: "enqueue 17"
    ("enqueue", 18),     # Enqueue 18, expected output: "enqueue 18"
    ("enqueue", 19),     # Enqueue 19, expected output: "enqueue 19"
    ("enqueue", 20),     # Enqueue 20, expected output: "enqueue 20"
    ("enqueue", 21),     # Try to enqueue into a full queue, expected output: "enqueue None"
    ("dequeue", 4),      # Dequeue 4, expected output: "dequeue 4"
    ("dequeue", 5),      # Dequeue 5, expected output: "dequeue 5"
    ("dequeue", 6),      # Dequeue 6, expected output: "dequeue 6"
    ("dequeue", 7),      # Dequeue 7, expected output: "dequeue 7"
    ("dequeue", 8),      # Dequeue 8, expected output: "dequeue 8"
    ("dequeue", 9),      # Dequeue 9, expected output: "dequeue 9"
    ("dequeue", 10),     # Dequeue 10, expected output: "dequeue 10"
    ("dequeue", 11),     # Dequeue 11, expected output: "dequeue 11"
    ("dequeue", 12),     # Dequeue 12, expected output: "dequeue 12"
    ("dequeue", 13),     # Dequeue 13, expected output: "dequeue 13"
    ("dequeue", 14),     # Dequeue 14, expected output: "dequeue 14"
    ("dequeue", 15),      # Dequeue 15, expected output: "dequeue 15"
]

operations2 = [
    ("peek", None),      # Peek into an empty queue, expected output: "peek None"
    ("dequeue", None),   # Try to dequeue from an empty queue, expected output: "dequeue None"
    ("enqueue", 1),      # Enqueue 1, expected output: "enqueue 1"
    ("enqueue", 2),      # Enqueue 2, expected output: "enqueue 2"
    ("enqueue", 3),      # Enqueue 3, expected output: "enqueue 3"
    ("peek", 1),         # Peek when queue is not empty, expected output: "peek 1"
    ("dequeue", 1),      # Dequeue 1, expected output: "dequeue 1"
    ("enqueue", 4),      # Enqueue 4, expected output: "enqueue 4"
    ("peek", 2),         # Peek front element (2), expected output: "peek 2"
    ("dequeue", 2),      # Dequeue 2, expected output: "dequeue 2"
    ("dequeue", 3),      # Dequeue 3, expected output: "dequeue 3"
    ("peek", 4),         # Peek front element (4), expected output: "peek 4"
    ("enqueue", 5),      # Enqueue 5, expected output: "enqueue 5"
    ("enqueue", 6),      # Enqueue 6, expected output: "enqueue 6"
    ("enqueue", 7),      # Enqueue 7, expected output: "enqueue 7"
    ("enqueue", 8),      # Enqueue 8, expected output: "enqueue 8"
    ("enqueue", 9),      # Enqueue 9, expected output: "enqueue 9"
    ("enqueue", 10),     # Enqueue 10, expected output: "enqueue 10"
    ("enqueue", 11),     # Enqueue 11, expected output: "enqueue 11"
    ("enqueue", 12),     # Enqueue 12, expected output: "enqueue 12"
    ("enqueue", 13),     # Enqueue 13, expected output: "enqueue 13"
    ("enqueue", 14),     # Enqueue 14, expected output: "enqueue 14"
    ("enqueue", 15),     # Enqueue 15, expected output: "enqueue 15"
    ("enqueue", 16),     # Enqueue 16, expected output: "enqueue 16"
    ("enqueue", 17),     # Enqueue 17, expected output: "enqueue 17"
    ("enqueue", 18),     # Enqueue 18, expected output: "enqueue 18"
    ("enqueue", 19),     # Enqueue 19, expected output: "enqueue 19"
    ("enqueue", 20),     # Enqueue 20, expected output: "enqueue 20"
    ("dequeue", 4),      # Dequeue 4, expected output: "dequeue 4"
    ("dequeue", 5),      # Dequeue 5, expected output: "dequeue 5"
    ("dequeue", 6),      # Dequeue 6, expected output: "dequeue 6"
    ("dequeue", 7),      # Dequeue 7, expected output: "dequeue 7"
    ("dequeue", 8),      # Dequeue 8, expected output: "dequeue 8"
    ("dequeue", 9),      # Dequeue 9, expected output: "dequeue 9"
    ("dequeue", 10),     # Dequeue 10, expected output: "dequeue 10"
    ("dequeue", 11),     # Dequeue 11, expected output: "dequeue 11"
    ("dequeue", 12),     # Dequeue 12, expected output: "dequeue 12"
    ("dequeue", 13),     # Dequeue 13, expected output: "dequeue 13"
    ("dequeue", 14),     # Dequeue 14, expected output: "dequeue 14"
    ("dequeue", 15),      # Dequeue 15, expected output: "dequeue 15"
]



# Test the implementations
print("Testing CircularQueueArray:")
queue = CircularQueueArray(17)
for operation, value in operations1:
    if operation == "enqueue":
        queue.enqueue(value)
    elif operation == "dequeue":
        queue.dequeue()
    elif operation == "peek":
        queue.peek()
    else:
        print("Invalid operation")

print("\nTesting CircularQueueLinkedList:")
queue = CircularQueueLinkedList()
for operation, value in operations2:
    if operation == "enqueue":
        queue.enqueue(value)
    elif operation == "dequeue":
        queue.dequeue()
    elif operation == "peek":
        queue.peek()
    else:
        print("Invalid operation")
