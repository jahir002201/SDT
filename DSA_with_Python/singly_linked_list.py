class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_head(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

def insert(head, pos, val):
    new_node = Node(val)
    tmp = head
    for _ in range(pos - 1):
        tmp = tmp.next
    new_node.next = tmp.next
    tmp.next = new_node

def insert_tail(head, tail, val):
    new_node = Node(val)
    if head is None:
        return new_node, new_node
    tail.next = new_node
    return head, new_node

def size(head):
    count = 0
    tmp = head
    while tmp:
        count += 1
        tmp = tmp.next
    return count

def delete_head(head):
    if head is None:
        return None
    return head.next

def delete_node(head, pos):
    if pos == 0:
        return delete_head(head)
    tmp = head
    for _ in range(pos - 1):
        tmp = tmp.next
    tmp.next = tmp.next.next
    return head

def bubble_sort_desc(head):
    i = head
    while i and i.next:
        j = i.next
        while j:
            if i.val < j.val:
                i.val, j.val = j.val, i.val
            j = j.next
        i = i.next

def print_linked_list(head):
    tmp = head
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()


values = [10, 3, 8, 15, 2]
head = None
tail = None

for v in values:
    head, tail = insert_tail(head, tail, v)

print("Original List: ", end="")
print_linked_list(head)

head = insert_head(head, 5)
print("After Insert Head (5): ", end="")
print_linked_list(head)

insert(head, 3, 7)
print("After Insert pos=3, val=7: ", end="")
print_linked_list(head)

head = delete_head(head)
print("After Delete Head: ", end="")
print_linked_list(head)

head = delete_node(head, 2)
print("After Delete pos=2: ", end="")
print_linked_list(head)

bubble_sort_desc(head)
print("After Sort (Descending): ", end="")
print_linked_list(head)

print("Size:", size(head))