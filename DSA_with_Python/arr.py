class Array:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._array = [None] * self._capacity

    def push_back(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = value
        self._size += 1

    def pop_back(self):
        if self._size == 0:
            raise IndexError("pop_back from empty array")
        value = self._array[self._size - 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return value

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def resize(self, new_size):
        if new_size > self._capacity:
            self._resize(new_size)
        elif new_size < self._size:
            for i in range(new_size, self._size):
                self._array[i] = None
        self._size = new_size

    def empty(self):
        return self._size == 0

    def at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]

    def front(self):
        if self.empty():
            raise IndexError("front from empty array")
        return self._array[0]

    def back(self):
        if self.empty():
            raise IndexError("back from empty array")
        return self._array[self._size - 1]

    def clear(self):
        for i in range(self._size):
            self._array[i] = None
        self._size = 0

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = value
        self._size += 1

    def erase(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._size - 1] = None
        self._size -= 1
    def begin(self):
        return 0
    def end(self):
        return self._size
    def rbegin(self):
        return self._size - 1
    def rend(self):
        return -1
    def swap(self, other):
        if not isinstance(other, Array):
            raise TypeError("swap argument must be an Array")
        self._array, other._array = other._array, self._array
        self._size, other._size = other._size, self._size
        self._capacity, other._capacity = other._capacity, self._capacity
    def shrink_to_fit(self):
        if self._size < self._capacity:
            self._resize(self._size)
    def reserve(self, new_capacity):
        if new_capacity > self._capacity:
            self._resize(new_capacity)
    def remove(self, value):
        i = 0
        while i < self._size:
            if self._array[i] == value:
                self.erase(i)
            else:
                i += 1
    def print_array(self):
        for i in range(self._size):
            print(self._array[i], end=' ')
        print()
    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity 
    def __getitem__(self, index):
        return self.at(index)
    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        self._array[index] = value
    def __len__(self):
        return self._size
    def __del__(self):
        del self._array
        self._size = 0
        self._capacity = 0

arr = Array()
arr.push_back(1)
arr.push_back(2)
arr.push_back(3)
arr.print_array()  # Output: 1 2 3
arr.insert(1, 4)
arr.print_array()  # Output: 1 4 2 3
arr.erase(2)
arr.print_array()  # Output: 1 4 3
print("Front:", arr.front())  # Output: Front: 1
print("Back:", arr.back())    # Output: Back: 3
print("Size:", arr.size())    # Output: Size: 3
print("Capacity:", arr.capacity())  # Output: Capacity: 4
arr.remove(4)
arr.print_array()  # Output: 1 3
arr.clear()
print("Empty:", arr.empty())  # Output: Empty: True