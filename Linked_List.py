"""This file seeks to code the linked list 
class and all it dependencies"""

# First is the node class and constructor

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Next the Linked List class

class LL:
    
    '''first thing at this point is to define the head that is the starting point of the linked list
    This would be found in the constructor of this class LL'''
    
    def __init__(self): 
        self.head = node()
    
    '''Next we define the methods or attributes of the Linked List such as
    Append (add) - Because we need to be able to add to our list
    Display (show) - Because we need to see what has been added. We need to be able to 
    view what is in our list
    Erase (rem) - Because we need to remove or delete elements we no longer need in our list
    Get - Incase we need to fetch an element from our list
    Length - To keep track of the size in numbers of elements of the list.
    
    Let's get to it'''

    def add(self, data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def show(self):
        elem = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elem.append(current_node.data)
        return elem

    def length(self):
        count = 0
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            count += 1
        return count


    def get(self,index):
        count = 0
        current_node = self.head
        if index>=self.length():
            return("Index out of range")
        else:
            while current_node.next != None:
                current_node = current_node.next
                if count == index: return current_node.data
                count += 1
                
                
    def rem(self, index):
        count = 0
        current_node = self.head
        
        if index>=self.length():
            return("Index out of range")
        else:
            while current_node.next != None:
                last_node = current_node
                current_node = current_node.next
                
                if count == index:
                    last_node.next = current_node.next
                    return
                count += 1

    
# Testing 

test = LL()
test.add(1)
test.add(4)
print(test.show())
test.length()
print(test.get(1))
test.rem(1)
print(test.show())
