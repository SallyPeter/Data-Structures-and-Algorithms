"""This file seeks to code the stack 
class and all it dependencies"""


class stack():
    def __init__(self): #creating the constructor
        self.stack = []
    
    def add_to_stack(self, value): #adding new values to the stack
        self.stack.append(value)
        # should incase you want only unique values in your stack, uncomment the if block below
        # if value not in self.stack:
        #     self.stack.append(value)
        #     return True
        return True
    
    def rem_from_stack(self): # removing elements from a stack
        """Note: Because stacks work on the last in first out principle, 
        we do not need an index or the particular value to be removed."""
        self.stack.pop()
    
    def show(self): #returns all the elements in the stack
        return(self.stack)

    def last(self): #shows the last element in the stack
        return(self.stack[-1])

# Test
try:
    stk = stack()
    stk.add_to_stack(1)
    print('stack now contains: ', stk.show())
    stk.add_to_stack(2)
    stk.add_to_stack(3)
    stk.add_to_stack(4)
    stk.add_to_stack(5)
    print('stack now contains: ', stk.show())
    stk.rem_from_stack()
    print('Last element in stack: ', stk.last())
    stk.rem_from_stack()
    print('stack now contains: ', stk.show())
    print("\nStack's looking good!")
except:
    print('You might have an error somewhere')

