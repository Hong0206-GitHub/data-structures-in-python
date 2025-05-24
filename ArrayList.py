class ArrayList:
    
    # Constructor: sets maximum capacity of the array
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    # Check array is empty
    # Return True if array is empty
    def isEmpty(self):
        return self.size == 0
    
    # Check array is full
    # Return True if array is full
    def isFull(self):
        return self.size == self.capacity

    # Return element at given index
    def getElement(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        return None
    
    # Insert elem into array at position index
    def insert(self, index, elem):
        if not self.isFull() and 0 <= index <= self.size:
            for i in range(self.size, index, -1):
                self.array[i] = self.array[i - 1]
            
            self.array[index] = elem
            self.size += 1

        else: 
            raise IndexError("Array is full or index is out of bounds")
        
    # Delete element at given index and return its value
    def delete(self, index):
        if not self.isEmpty() and 0 <= index < self.size:
            value = self.array[index]
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]   
            self.size -= 1
            return value
        else:
            raise IndexError("Array is empty or index is out of bounds")
        
    # Return string representation of the list (only valid elements)
    def __str__(self):
        return str(self.array[0:self.size])
    



# test code
if __name__ == "__main__":
    alist = ArrayList(5)
    alist.insert(0, 10)
    alist.insert(1, 20)
    alist.insert(1, 15)
    print(alist)  # [10, 15, 20]
    alist.delete(1)
    print(alist)  # [10, 20]