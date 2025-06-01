class CircularQueue:

    # Constructor: sets maximum capacity of the queue
    # front points to the position before the first element
    # rear points to the last inserted element
    def __init__(self, capacity=101):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0

    # Check queue is empty
    # Return True if queue is empty
    def is_empty(self):
        return self.front == self.rear

    # Check queue is full
    # Return True if queue is full
    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity

    # Add an element to the end of the queue.
    # Raises OverflowError if the queue has reached its maximum capacity.
    def enqueue(self, elem):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = elem
        else:
            raise OverflowError("Queue is full")

    # Remove and return the first element of the queue
    # Raises IndexError if the queue is empty
    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            value = self.queue[self.front]
            self.queue[self.front] = None
            
            return value
        else:
            raise IndexError("Queue is empty")
        
    # Return the front element of the queue without removing it.
    # Raises IndexError if the queue is empty.        
    def peek(self):
        if not self.is_empty():
            return self.queue[(self.front + 1) % self.capacity]
        else:
            raise IndexError("Queue is empty")

    # Return string representation of the queue (only valid elements)
    def __str__(self):
        if self.is_empty():
            return "[]"
        elif self.front < self.rear:
            return str(self.queue[self.front + 1:self.rear + 1])
        else:
            return str(self.queue[self.front + 1:self.capacity] + self.queue[0:self.rear + 1])


    # Return the number of elements currently in the queue
    def size(self):
        pass

    # Remove all elements from the queue and reset it to empty state
    def clear(self):
        pass

    # Return True if element is present in the queue
    def contains(self, elem):
        pass

    # Return a list of all valid elements in queue order
    def to_list(self):
        pass

    # Return the capacity of the queue
    def get_capacity(self):
        pass






if __name__ == "__main__":
    # Create a queue with capacity 5
    cq = CircularQueue(5)

    # Enqueue elements
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    print("After enqueue 10, 20, 30:", cq)

    # Dequeue elements
    print("Dequeued:", cq.dequeue())
    print("After dequeue:", cq)

    # Enqueue more elements
    cq.enqueue(40)
    cq.enqueue(50)
    print("After enqueue 40, 50:", cq)

    # Check if queue is full
    print("Is full?", cq.is_full())

    # Try to enqueue to a full queue (should raise OverflowError)
    try:
        cq.enqueue(60)
    except OverflowError as e:
        print("Error:", e)

    # Peek front element
    print("Peek:", cq.peek())

    # Check if queue is empty
    print("Is empty?", cq.is_empty())

    # # Check size of the queue
    # print("Size:", cq.size())

    # # Clear the queue
    # cq.clear()
    # print("After clear:", cq)

    # # Check contains
    # print("Contains 20?", cq.contains(20))
    # print("Contains 100?", cq.contains(100))

    # # Get list of elements
    # print("Elements in queue:", cq.to_list())

    # # Get capacity
    # print("Capacity:", cq.get_capacity())
