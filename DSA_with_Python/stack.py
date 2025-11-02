class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def top(self):
        if self.head is None:
            return None
        return self.head.val

    def empty(self):
        return self.head is None

s = Stack()
s.push(10)
s.push(20)
print(s.top())  # 20
s.pop()
print(s.top())  # 10