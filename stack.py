__author__ = 'Robert Morris'

import time

class Stack:

    def __init__(self):
        '''Creates a new stack that is empty.'''
        self.items = []

    def isEmpty(self):
        '''tests to see whether the stack is empty.
        returns boolean varible.'''
        return self.items == []

    def push(self, item):
        '''Adds a new item to the top of the stack. The stack is modified'''
        self.items.append(item)

    def pop(self):
        '''Return the top item from the stack and remove it.'''
        return self.items.pop()

    def peek(self):

        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)



# if __name__ == '__main__':
