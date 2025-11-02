class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def insert_tail(head, tail, val):
    new_node = Node(val)
    if head is None:
        return new_node, new_node
    tail.next = new_node
    new_node.prev = tail
    return head, new_node

def insert_head(head, tail, val):
    new_node = Node(val)
    if head is None:
        return new_node, new_node
    new_node.next = head
    head.prev = new_node
    return new_node, tail

def insert_node(head, tail, pos, val):
    if pos == 0:
        return insert_head(head, tail, val)
    new_node = Node(val)
    tmp = head
    for _ in range(pos - 1):
        tmp = tmp.next
    new_node.next = tmp.next
    new_node.prev = tmp
    if tmp.next:
        tmp.next.prev = new_node
    else:
        tail = new_node
    tmp.next = new_node
    return head, tail

def delete_head(head, tail):
    if head is None:
        return None, None
    nxt = head.next
    if nxt:
        nxt.prev = None
        return nxt, tail
    else:
        return None, None

def delete_node(head, tail, pos):
    if head is None:
        return None, None
    if pos == 0:
        return delete_head(head, tail)
    tmp = head
    for _ in range(pos):
        tmp = tmp.next
    if tmp is None:
        return head, tail
    if tmp.prev:
        tmp.prev.next = tmp.next
    if tmp.next:
        tmp.next.prev = tmp.prev
    if tmp == tail:
        tail = tmp.prev
    return head, tail

def bubble_sort_desc(head):
    i = head
    while i:
        j = i.next
        while j:
            if i.val < j.val:
                i.val, j.val = j.val, i.val
            j = j.next
        i = i.next

def print_forward(head):
    tmp = head
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()

def print_backward(tail):
    tmp = tail
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.prev
    print()


values = [10, 3, 8, 15, 2]
head, tail = None, None
for v in values:
    head, tail = insert_tail(head, tail, v)

print("Forward: ", end="")
print_forward(head)
print("Backward: ", end="")
print_backward(tail)

head, tail = insert_head(head, tail, 5)
print("After Insert Head (5): ", end="")
print_forward(head)

head, tail = insert_node(head, tail, 3, 7)
print("After Insert pos=3, val=7: ", end="")
print_forward(head)

head, tail = delete_head(head, tail)
print("After Delete Head: ", end="")
print_forward(head)

head, tail = delete_node(head, tail, 2)
print("After Delete pos=2: ", end="")
print_forward(head)

bubble_sort_desc(head)
print("After Sort (Descending): ", end="")
print_forward(head)
