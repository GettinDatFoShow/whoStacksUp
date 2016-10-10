__author__ = 'Janelle Boyd'

import time
import random

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

    def createStack(self, stackSize, minRange, maxRange):
        for i in range(stackSize):
            self.push(random.randint(minRange, maxRange))
        return self.items

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)
