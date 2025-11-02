import sys

def insert_heap(heap, val):
    heap.append(val)
    cur_idx = len(heap) - 1
    while cur_idx != 0:
        parent_idx = (cur_idx - 1) // 2
        if heap[parent_idx] < heap[cur_idx]:
            heap[parent_idx], heap[cur_idx] = heap[cur_idx], heap[parent_idx]
        else:
            break
        cur_idx = parent_idx

def print_heap(heap):
    print(" ".join(map(str, heap)))

def delete_heap(heap):
    if not heap:
        print("Heap is empty!")
        return
    print(f"{heap[0]} Deleted.")
    heap[0] = heap[-1]
    heap.pop()
    cur_idx = 0

    while True:
        left_idx = 2 * cur_idx + 1
        right_idx = 2 * cur_idx + 2

        left_val = heap[left_idx] if left_idx < len(heap) else -sys.maxsize
        right_val = heap[right_idx] if right_idx < len(heap) else -sys.maxsize

        if left_val > right_val and left_val > heap[cur_idx]:
            heap[left_idx], heap[cur_idx] = heap[cur_idx], heap[left_idx]
            cur_idx = left_idx
        elif right_val > left_val and right_val > heap[cur_idx]:
            heap[right_idx], heap[cur_idx] = heap[cur_idx], heap[right_idx]
            cur_idx = right_idx
        else:
            break


heap = []
n = int(input("Enter number of elements: "))
print(f"Enter {n} elements:")
for _ in range(n):
    val = int(input())
    insert_heap(heap, val)

print("Heap after insertion:")
print_heap(heap)

delete_heap(heap)
print("Heap after deletion:")
print_heap(heap)