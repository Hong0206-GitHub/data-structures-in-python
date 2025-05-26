class ArrayDeque:

    # Constructor: sets maximum capacity of the deque
    # front points to the first element in the deque (always 0 in this implementation)
    # rear points to the last inserted element in the deque
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.deque = [None] * capacity
        self.front = 0
        self.rear = -1

    # Check deque is empty
    # Return True if deque is empty
    def is_empty(self):
        return self.rear == -1

    # Check deque is full
    # Return True if deque is full
    def is_full(self):
        return self.rear == self.capacity - 1

    # Return deque's size
    def get_size(self):
        return self.rear + 1

    # Return string representation of the deque (only valid elements)
    def __str__(self):
        if not self.is_empty():
            return str(self.deque[self.front:self.rear + 1])
        else:
            return "[]"

    # Add an element to the front of the deque.
    # Raises OverflowError if the deque has reached its maximum capacity.       
    def add_front(self, elem):
        if not self.is_full():
            for i in range(self.rear + 1, self.front, -1):
                self.deque[i] = self.deque[i - 1]
            self.deque[self.front] = elem
            self.rear += 1
        else:
            raise OverflowError("Deque is full")
        
    # Return the front element of the deque without removing it.
    # Raises IndexError if the deque is empty.        
    def peek_front(self):
        if not self.is_empty():
            return self.deque[self.front]
        else:
            raise IndexError("Deque is empty")

    # Remove and return the first element of the deque
    # Raises IndexError if the deque is empty        
    def remove_front(self):
        if not self.is_empty():
            value = self.deque[self.front]
            for i in range(self.front, self.rear):
                self.deque[i] = self.deque[i + 1]
            self.deque[self.rear] = None
            self.rear -= 1
            return value
        else:
            raise IndexError("Deque is empty")

    # Add an element to the end of the deque.
    # Raises OverflowError if the deque has reached its maximum capacity.
    def add_rear(self, elem):
        if not self.is_full():
            self.rear += 1
            self.deque[self.rear] = elem
        else:
            raise OverflowError("Deque is full")        

    # Return the last element of the deque without removing it.
    # Raises IndexError if the deque is empty.
    def peek_rear(self):
        if not self.is_empty():
            return self.deque[self.rear]
        else:
            raise IndexError("Deque is empty")

    # Remove and return the last element of the deque
    # Raises IndexError if the deque is empty
    def remove_rear(self):
        if not self.is_empty():
            value = self.deque[self.rear]
            self.deque[self.rear] = None
            self.rear -= 1
            return value
        else:
            raise IndexError("Deque is empty")

    # Removes all elements from the deque and resets it to empty state
    def clear(self):
        pass

    # Returns True if the element exists in the deque
    def contains(self, elem):
        pass

    # Returns a list of valid elements in the deque (from front to rear)
    def to_list(self):
        pass

    # Returns the index of the front element
    def get_front_index(self):
        pass

    # Returns the index of the rear element
    def get_rear_index(self):
        pass

    # Returns True if the given element is at the front
    def is_front(self, elem):
        pass

    # Returns True if the given element is at the rear
    def is_rear(self, elem):
        pass


if __name__ == "__main__":
    print("=== ArrayDeque Test ===")
    dq = ArrayDeque(5)

    # Test: add elements to front and rear
    dq.add_rear(10)
    dq.add_front(5)
    dq.add_rear(15)
    print("Deque after add_front and add_rear:", dq)  # [5, 10, 15]

    # Test: peek front and rear
    print("Front element (peek):", dq.peek_front())  # 5
    print("Rear element (peek):", dq.peek_rear())    # 15

    # Test: remove front and rear
    print("Removed from front:", dq.remove_front())  # 5
    print("Removed from rear:", dq.remove_rear())    # 15
    print("Deque after removals:", dq)               # [10]

    # Test: get_size
    print("Current size:", dq.get_size())  # 1

    # Test: clear (currently not implemented)
    # dq.clear()
    # print("Deque after clear:", dq)  # []

    # Test: contains (currently not implemented)
    # print("Contains 10?", dq.contains(10))  # True
    # print("Contains 99?", dq.contains(99))  # False

    # Test: to_list (currently not implemented)
    # print("Deque as list:", dq.to_list())  # [10]

    # Test: get_front_index and get_rear_index (not implemented)
    # print("Front index:", dq.get_front_index())  # Expected: 0
    # print("Rear index:", dq.get_rear_index())    # Expected: 0

    # Test: is_front and is_rear (not implemented)
    # print("Is 10 at front?", dq.is_front(10))  # True
    # print("Is 10 at rear?", dq.is_rear(10))    # True