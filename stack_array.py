class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity        #Capacity of the stack
        self.items = [None]*capacity    #Initializing the stack
        self.num_items = 0              #Number of elements in the stack

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0              #works

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity  #works

    def push(self, item):
        '''If stack is not full, pushes item on stack.
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_full():                  #works
            self.num_items += 1
            self.items[self.num_items - 1] = item
        else:
            raise IndexError

    def pop(self):
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_empty():                 #works
            self.num_items -= 1
            return self.items[self.num_items]
        else:
            raise IndexError

    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if not self.is_empty():                 #works
            return self.items[self.num_items-1]
        else:
            raise IndexError

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items                 #works

