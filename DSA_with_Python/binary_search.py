def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return False

# Input number of elements and queries
n, q = map(int, input().split())
arr = list(map(int, input().split()))

# Sort the array
arr.sort()

# Process queries
for _ in range(q):
    x = int(input())
    if binary_search(arr, x):
        print("Found")
    else:
        print("Not Found")