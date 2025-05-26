# 📚 Data Structures in Python

This repository contains implementations of fundamental data structures in Python.  
Each data structure is implemented from scratch without using built-in collection libraries (like `list`, `set`, or `dict`) beyond necessary array operations.

## 📂 Structure

```
.
├── ArrayList.py
├── ArraySet.py
├── ArrayStack.py
├── ArrayQueue.py
├── ArrayDeque.py
└── README.md
```

## ✅ Implemented Data Structures

| File Name        | Data Structure | Description                                                      | Time Complexity (Average)                  |
|------------------|----------------|------------------------------------------------------------------|--------------------------------------------|
| `ArrayList.py`   | Array List     | Dynamic array with append, insert, delete                        | Access O(1), Insert/Delete O(n)            |
| `ArraySet.py`    | Array Set      | Set using list (no duplicates allowed)                           | Search/Insert/Delete O(n)                  |
| `ArrayStack.py`  | Array Stack    | Stack (LIFO) using array                                         | Push/Pop/Peek O(1)                         |
| `ArrayQueue.py`  | Array Queue    | Queue (FIFO) using array (shift elements on dequeue)             | Enqueue O(1), Dequeue O(n)                 |
| `ArrayDeque.py`  | Array Deque    | Double-ended queue (front/rear enqueue and dequeue)              | All operations amortized O(1)              |

> 🔸 All classes are implemented using basic Python constructs and support common operations such as `is_empty()`, `size()`, and `__str__()` where applicable.

---

## 🏗️ Planned Features

- [ ] CircularQueue
- [ ] PriorityQueue (Max-Heap)
- [ ] LinkedList (Singly, Doubly)
- [ ] Binary Tree (with traversal)
- [ ] Hash Table (with linear/quadratic probing)

---

## 🧪 Usage Examples

### 🔹 ArrayList
```python
from ArrayList import ArrayList

arr = ArrayList()
arr.append(1)
arr.insert(0, 10)
print(arr)  # Output: [10, 1]
```

### 🔹 ArraySet
```python
from ArraySet import ArraySet

s = ArraySet()
s.add(5)
s.add(5)
print(s.contains(5))  # Output: True
print(s)  # Output: [5]
```

### 🔹 ArrayStack
```python
from ArrayStack import ArrayStack

stack = ArrayStack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
```

### 🔹 ArrayQueue
```python
from ArrayQueue import ArrayQueue

q = ArrayQueue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
```

### 🔹 ArrayDeque
```python
from ArrayDeque import ArrayDeque

dq = ArrayDeque()
dq.add_front(1)
dq.add_rear(2)
print(dq.remove_front())  # Output: 1
```

---

## 📄 License

MIT License
