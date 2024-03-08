import random
import timeit
import matplotlib.pyplot as plt
import numpy as np 

#question 1 
class Priority_Queue_Array:
    #initialie the new instance to hold the items of the queue 
    def __init__(self):
        self.items = []

    #add items to the queue 
    def enqueue(self, item):
        self.items.append(item)
        self.items.sort()

    #pop the first item 
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    #check for exmpty array
    def is_empty(self):
        return len(self.items) == 0

#question 2 
class Priority_Queue_2:
    
    #set up new instance to hold items of queue 
    def __init__(self):
        self.items = []

    #add item 
    #find the correct postion to insert 
    def enqueue(self, item):
        if len(self.items) == 0:
            self.items.append(item)
        else:
            index = 0
            while index < len(self.items) and self.items[index] < item:
                index += 1
            self.items.insert(index, item)

    #pop the first element from the iinternal list 
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    #check if empty
    def is_empty(self):
        return len(self.items) == 0

def generate_random_tasks(length=1000, enqueue_prob=0.7):
    #generate array of numbers between 0 and 1 
    random_numbers = np.random.rand(length)
    #assign random numbers to task 
    tasks = ['enqueue' if num < enqueue_prob else 'dequeue' for num in random_numbers]
    return tasks

def perform_tasks(queue, tasks):
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(random.randint(1, 100))  #when the tska equals we enqueue from 1-100 times 
        else:
            queue.dequeue()    #otherwise we dequeue

# Question 3 
def measure_performance(queue_class, tasks):
    queue = queue_class()
    start_time = timeit.default_timer()
    perform_tasks(queue, tasks)
    end_time = timeit.default_timer()
    return end_time - start_time


#question 4 
#performance of the sorted priority queue 
sorted_queue_times = []
for _ in range(100):
    tasks = generate_random_tasks()
    time_taken = measure_performance(Priority_Queue_2, tasks)
    sorted_queue_times.append(time_taken)

#performance of the regualr priority queue 
array_queue_times = []
for _ in range(100):
    tasks = generate_random_tasks()
    time_taken = measure_performance(Priority_Queue_Array, tasks)
    array_queue_times.append(time_taken)



# Plot the distribution of times
plt.scatter(range(100), sorted_queue_times, alpha=0.5, label='Priority_Queue_Sorted', color='purple')
plt.scatter(range(100), array_queue_times, alpha=0.5, label='Priority_Queue_Array', color= 'red')

#i attempted to chang ethe scale to increase readability but it did not work
# plt.xticks(range(0, 101, 5))
# plt.yticks(range(0, 101, 5))

plt.legend(loc='upper left')
plt.xlabel('Number of Trial')
plt.ylabel('Time in Seconds (s)')
plt.title('Performance of priority queue specifically Sorted vs. Not')
plt.show()


#question 5 
"""
As evident in the graphical analysis; the unsorted priority array is faster in the enqueue. 
This is because there isn't any extra time used in attempts to sort the array before appending to the array.

However, the sorted priority array is faster in the dequeue because of the way in which it is sorted. It 
aids the removal process as it encourages a constant-time in the removal process
"""
