# Python Data Structures

This repository contains basic data structure implementations written in Python from scratch.

## ✅ Completed

- [x] ArrayList

## 🚧 Upcoming (planned)

- [ ] Queue
- [ ] Stack
- [ ] Deque
- [ ] LinkedList
- [ ] Binary Tree
- [ ] Hash Table

## Example (ArrayList)

```python
from ArrayList import ArrayList

alist = ArrayList(5)
alist.insert(0, 10)
alist.insert(1, 20)
print(alist)  # [10, 20]
alist.delete(0)
print(alist)  # [20]
