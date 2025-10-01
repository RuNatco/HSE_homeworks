class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.start = None
        self.finish = None

    def is_empty(self):
        return self.start is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.finish is None:
            self.start = self.finish = new_node
            return
        self.finish.next = new_node
        self.finish = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self.start.value
        self.start = self.start.next
        if self.start is None:
            self.finish = None
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.start.value
