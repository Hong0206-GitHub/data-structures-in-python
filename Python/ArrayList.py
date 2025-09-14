class ArrayList:
    
    # Constructor: sets maximum capacity of the array
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    # Check array is empty
    # Return True if array is empty
    def is_empty(self):
        return self.size == 0
    
    # Check array is full
    # Return True if array is full
    def is_full(self):
        return self.size == self.capacity

    # Return element at given index
    def get_element(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        return None
    
    # Insert elem into array at position index if it is not full and index is not out of bounds
    def insert(self, index, elem):
        if not self.is_full() and 0 <= index <= self.size:
            for i in range(self.size, index, -1):
                self.array[i] = self.array[i - 1]
            
            self.array[index] = elem
            self.size += 1

        else: 
            raise IndexError("Array is full or index is out of bounds")
        
    # Delete element at given index and return its value
    def delete(self, index):
        if not self.is_empty() and 0 <= index < self.size:
            value = self.array[index]
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]   
            self.size -= 1
            return value
        else:
            raise IndexError("Array is empty or index is out of bounds")
        
    # Returns the index of the given element, or -1 if not found
    def index_of(self, elem):
        for i in range(self.size):
            if elem == self.array[i]:
                return i
        return -1

    # Clears all elements in the array
    def clear(self):
        self.array = [None] * self.capacity
        self.size = 0

    # Replaces the element at the given index with a new value
    def replace(self, index, elem):
        if 0 <= index < self.size:
            self.array[index] = elem
        else:
            raise IndexError("Index out of bounds")

    # Converts the array list to a regular Python list
    def to_list(self):
        return list(self.array[:self.size])

    # Returns True if the element exists in the array
    def contains(self, elem):
        return self.index_of(elem) != -1 

    
    # Return string representation of the list (only valid elements)
    def __str__(self):
        return str(self.array[0:self.size])
    


# test code
# Create an ArrayList with capacity 5
# Insert elements at specific positions
# Delete an element at index 1
if __name__ == "__main__":
    alist = ArrayList(5)
    alist.insert(0, 10)
    alist.insert(1, 20)
    alist.insert(1, 15)
    print(alist)  # [10, 15, 20]
    alist.delete(1)
    print(alist)  # [10, 20]
    
    # Test: index_of()
    print(alist.index_of(10))  # Expected output: 0 (10 is at index 0)
    print(alist.index_of(99))  # Expected output: -1 (99 is not in the list)

    # Test: contains()
    print(alist.contains(20))  # Expected output: True
    print(alist.contains(99))  # Expected output: False

    # Test: replace()
    alist.replace(1, 30)       
    print(alist)  # Expected output: [10, 30] (20 replaced with 30)

    # Test: to_list()
    print(alist.to_list())  # Expected output: [10, 30]

    # Test: clear()
    alist.clear()
    print(alist)         # Expected output: [] (list is cleared)
    print(alist.is_empty())  # Expected output: True
