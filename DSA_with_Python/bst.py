from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.val:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root

def search(root, x):
    if root is None:
        return False
    if root.val == x:
        return True
    elif x < root.val:
        return search(root.left, x)
    else:
        return search(root.right, x)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def level_order(root):
    if root is None:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

def height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


root = Node(10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 18)

print("Inorder Traversal:", end=" ")
inorder(root)
print()

print("Level Order Traversal:", end=" ")
level_order(root)
print()

val_to_search = 7
if search(root, val_to_search):
    print(f"{val_to_search} found in the tree.")
else:
    print(f"{val_to_search} not found in the tree.")

print("Total nodes in the tree:", count_nodes(root))
print("Total leaf nodes in the tree:", count_leaf_nodes(root))
print("Height of the tree:", height(root))