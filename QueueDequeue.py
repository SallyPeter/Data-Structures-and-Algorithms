"""This file seeks to code the Queue 
class and all it dependencies as well as the Dequeue"""

import collections as col

class queue():
    def __init__(self): #object constructor
        self.queue = []
    
    def add_to_q(self, value):
        self.queue.insert(0,value) # this ensures that new elements are only entered at index 0 (one end only)
        # should incase you want only unique values in your queue, uncomment the if block below
        # if value not in self.queue:
        #     self.queue.insert(0,value)
        #     return True
        return True
    
    def rem_from_q(self):
        if len(self.queue)>0:
            self.queue.pop()
        else:
            print('Queue is empty')
    
    def show(self): #returns all the elements in the queue
        if len(self.queue)>0:
            return(self.queue)
        else:
            print('Queue is empty!')

    def last(self): #shows the last element in the queue
        if len(self.queue)>0:
            return(self.queue[-1])
        else:
            print('Queue is empty!')
    
    def first(self): #shows the first element in the queue
        if len(self.queue)>0:
            return(self.queue[0])
        else:
            print('Queue is empty!')

# Dequeue 

deq = col.deque([])
deq.append(1)
print('Deque now contains: ', deq)
deq.append(2)
deq.appendleft(3)
deq.appendleft(4)
print('Deque now contains: ', deq)
deq.insert(2,5)
print('Deque now contains: ', deq)
deq.insert(0,7)
print('Deque now contains: ', deq)
deq.remove(2)
print('Deque now contains: ', deq)
deq.pop()
print('Deque now contains: ', deq)
deq.popleft()
print('Deque now contains: ', deq)

print('\n')




# Test
try:
    que = queue()
    que.add_to_q(1)
    print('Queue now contains: ', que.show())
    que.add_to_q(2)
    que.add_to_q(3)
    que.add_to_q(4)
    que.add_to_q(5)
    print('Queue now contains: ', que.show())
    que.rem_from_q()
    print('Last element in Queue: ', que.last())
    que.rem_from_q()
    print('Queue now contains: ', que.show())
    print("\nQueue's looking good!")
except:
    print('You might have an error somewhere')


