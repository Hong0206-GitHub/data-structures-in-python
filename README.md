# Python Data Structures

This repository contains basic data structure implementations written in Python from scratch.

## ✅ Completed

- [x] ArrayList

## 🚧 Upcoming (planned)


- [ ] ArraySet
- [ ] ArrayStack
- [ ] ArrayQueue
- [ ] ArrayDeque
- [ ] CircularQueue
- [ ] PriorityQueue
- [ ] CircularDeque
- [ ] LinkedList
- [ ] Binary Tree
- [ ] Hash Table

## Example (ArrayList)

```python
from ArrayList import ArrayList

alist = ArrayList(5)
alist.insert(0, 10)
alist.insert(1, 20)
alist.insert(1, 15)
print(alist)  # [10, 15, 20]
alist.delete(1)
print(alist)  # [10, 20]

# Test: indexOf()
print(alist.indexOf(10))  # Expected output: 0 (10 is at index 0)
print(alist.indexOf(99))  # Expected output: -1 (99 is not in the list)

# Test: contains()
print(alist.contains(20))  # Expected output: True
print(alist.contains(99))  # Expected output: False

# Test: replace()
alist.replace(1, 30)       
print(alist)  # Expected output: [10, 30] (20 replaced with 30)

# Test: toList()
print(alist.toList())  # Expected output: [10, 30]

# Test: clear()
alist.clear()
print(alist)         # Expected output: [] (list is cleared)
print(alist.isEmpty())  # Expected output: True
