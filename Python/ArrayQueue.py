class ArrayQueue:
    
    # Constructor: sets maximum capacity of the queue
    # front points to the first element in the queue (always 0 in this implementation)
    # rear points to the last inserted element in the queue
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1

    # Check queue is empty
    # Return True if queue is empty
    def is_empty(self):
        return self.rear == -1

    # Check queue is full
    # Return True if queue is full
    def is_full(self):
        return self.rear == self.capacity - 1

    # Add an element to the end of the queue.
    # Raises OverflowError if the queue has reached its maximum capacity.
    def enqueue(self, elem):
        if not self.is_full():
            self.rear += 1
            self.queue[self.rear] = elem
        else:
            raise OverflowError("Queue is full")

    # Remove and return the first element of the queue
    # Raises IndexError if the queue is empty
    def dequeue(self):
        if not self.is_empty():
            value = self.queue[self.front]
            for i in range(self.front, self.rear):
                self.queue[i] = self.queue[i + 1]
            self.queue[self.rear] = None
            self.rear -= 1
            return value
        else:
            raise IndexError("Queue is empty")

    # Return the front element of the queue without removing it.
    # Raises IndexError if the queue is empty.
    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty")

    # Return string representation of the queue (only valid elements)
    def __str__(self):
        if not self.is_empty():
            return str(self.queue[self.front:self.rear + 1])
        else:
            return "[]"
        
    # Returns the number of elements in the queue (from front to rear)
    def size(self):
        return self.rear + 1 if not self.is_empty() else 0
    
    # Removes all elements from the queue and resets it to empty state
    def clear(self):
        self.rear = -1
        self.queue = [None] * self.capacity
        
    # Returns a list of the valid elements in the queue (in order)
    def to_list(self):
        return list(self.queue[self.front:self.rear + 1])
    
    # Returns True if the given element exists in the queue
    def contains(self, elem):
        for i in range(self.rear + 1):
            if elem == self.queue[i]:
                return True
        return False
    
    # Returns True if the given element is at the front of the queue
    def is_front(self, elem):
        return self.queue[self.front] == elem
    
    # Returns True if the given element exists in the queue
    def is_rear(self, elem):
        return self.queue[self.rear] == elem
    
    




# test code
if __name__ == "__main__":
    print("=== ArrayQueue Test ===")

    q = ArrayQueue(5)

    # Test: enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue after enqueues:", q)  # [10, 20, 30]

    # Test: peek
    print("Front element (peek):", q.peek())  # 10

    # Test: size
    print("Current size:", q.size())  # 3

    # Test: to_list
    print("Queue as list:", q.to_list())  # [10, 20, 30]

    # Test: contains
    print("Contains 20?", q.contains(20))  # True
    print("Contains 40?", q.contains(40))  # False

    # Test: is_front
    print("Is 10 at front?", q.is_front(10))  # True
    print("Is 20 at front?", q.is_front(20))  # False

    # Test: is_rear
    print("Is 30 at rear?", q.is_rear(30))  # True
    print("Is 20 at rear?", q.is_rear(20))  # False

    # Test: dequeue
    print("Dequeued:", q.dequeue())  # 10
    print("Queue after dequeue:", q)  # [20, 30]

    # Test: clear
    q.clear()
    print("Queue after clear:", q)  # []

    # Test: is_empty after clear
    print("Is empty?", q.is_empty())  # True

    # Test: peek on empty (should raise error)
    try:
        q.peek()
    except IndexError as e:
        print("Expected error (peek on empty):", e)

    # Test: dequeue on empty (should raise error)
    try:
        q.dequeue()
    except IndexError as e:
        print("Expected error (dequeue on empty):", e)

    # Test: fill the queue to capacity
    for i in range(5):
        q.enqueue(i)
    print("Queue after filling:", q)  # [0, 1, 2, 3, 4]

    # Test: enqueue on full (should raise error)
    try:
        q.enqueue(99)
    except OverflowError as e:
        print("Expected error (enqueue on full):", e)
