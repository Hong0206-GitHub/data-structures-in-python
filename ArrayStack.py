class ArrayStack:

    # Constructor: sets maximum capacity of the stack
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    # Check if the stack is empty
    # Returns True if it is empty
    def is_empty(self):
        return self.top == -1
    
    # Check if the stack is full
    # Returns True if it is full
    def is_full(self):
        return self.top == self.capacity - 1
        
    # Push element onto the stack if it is not full
    # Raises OverflowError if the stack is full
    def push(self, elem):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = elem
        else:
            raise OverflowError("Stack is full")
    
    # Remove and return the top element of the stack
    # Raises IndexError if the stack is empty
    def pop(self):
        if not self.is_empty():
            value = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return value
        else:
            raise IndexError("Stack is empty")

    # Return the top element without removing it
    # Raises IndexError if the stack is empty
    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        else:
            raise IndexError("Stack is empty")
        
    # Returns the number of elements in the stack
    def size(self):
        return self.top + 1

    # Removes all elements from the stack
    def clear(self):
        self.top = -1
        self.stack = [None] * self.capacity

    # Returns a list of the elements in the stack (bottom to top)
    def to_list(self):
        return self.stack[:self.top + 1]

    # Return string representation of the stack (only valid elements)
    def __str__(self):
        return str(self.stack[0:self.top + 1])
    

    
# test code
if __name__ == "__main__":
    print("=== ArrayStack Test ===")
    
    stack = ArrayStack(5)

    # Test: push
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack)  # [10, 20, 30]

    # Test: peek
    print("Top element (peek):", stack.peek())  # 30

    # Test: size
    print("Current size:", stack.size())  # 3

    # Test: to_list
    print("Stack as list:", stack.to_list())  # [10, 20, 30]

    # Test: pop
    print("Popped:", stack.pop())  # 30
    print("Stack after pop:", stack)  # [10, 20]

    # Test: is_empty
    print("Is empty?", stack.is_empty())  # False

    # Test: clear
    stack.clear()
    print("Stack after clear:", stack)  # []

    # Test: is_empty after clear
    print("Is empty after clear?", stack.is_empty())  # True

    # Test: peek on empty (should raise error)
    try:
        stack.peek()
    except IndexError as e:
        print("Expected error (peek on empty):", e)

    # Test: pop on empty (should raise error)
    try:
        stack.pop()
    except IndexError as e:
        print("Expected error (pop on empty):", e)

    # Test: push until full
    for i in range(5):
        stack.push(i)
    print("Stack filled:", stack)  # [0, 1, 2, 3, 4]

    # Test: push on full (should raise error)
    try:
        stack.push(99)
    except OverflowError as e:
        print("Expected error (push on full):", e)
