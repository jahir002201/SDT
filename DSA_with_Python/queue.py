class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Queue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, val):
        new_node = Node(val)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return None
        return self.head.val

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.front())  # 10
q.dequeue()
print(q.front())  # 20