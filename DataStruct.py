__author__ = 'aouyang1'

from Node import Node
import ipdb


class TreeNode(object):

    def __init__(self, item, left=None, right=None):
        self.left = left
        self.right = right
        self.data = item


class StackClass(object):

    def __init__(self):
        self.top = None
        self.num_elem = 0
        self.min_top = None

    def push(self, item):
        if not self.top:
            self.top = Node(item)
            self.min_top = Node(item)
        else:
            # push item to top of stack
            old_top = self.top
            self.top = Node(item)
            self.top.next = old_top

            # node with minimum value in stack to top
            old_min = self.min_top
            if self.min_top.data > item:
                new_min = item
            else:
                new_min = self.min_top.data
            self.min_top = Node(new_min)
            self.min_top.next = old_min

        self.num_elem += 1

    def pop(self):
        if not self.top:
            return None
        else:
            item = self.top.data
            self.top = self.top.next

            self.min_top = self.min_top.next

            self.num_elem -= 1
            return item

    def peek(self):
        if not self.top:
            return None
        else:
            item = self.top.data
            return item

    def is_empty(self):
        return not self.top

    def size(self):
        return self.num_elem

    def min(self):
        if self.top:
            return self.min_top.data
        else:
            return None


class QueueClass(object):

    def __init__(self):
        self.front = None
        self.rear = None
        self.num_elem = 0

    def enqueue(self, item):
        if not self.rear:
            self.rear = Node(item)
            self.front = self.rear
        else:
            old_rear = self.rear
            self.rear = Node(item)
            self.rear.next = old_rear
            old_rear.prev = self.rear

        self.num_elem += 1

    def dequeue(self):
        if not self.front:
            return None
        else:
            item = self.front.data
            print self.front.prev, self.size()
            self.front = self.front.prev
            self.front.next = None
            self.num_elem -= 1
            return item

    def is_empty(self):
        return not self.rear

    def size(self):
        return self.num_elem


def sort_stack(s1):
    s2 = StackClass()

    while not s1.is_empty():

        if s2.is_empty() or s1.peek() >= s2.peek():
            s2.push(s1.pop())
        else:
            temp_val = s1.pop()
            while not s2.is_empty() and temp_val < s2.peek():

                s1.push(s2.pop())
            s2.push(temp_val)

    return s2