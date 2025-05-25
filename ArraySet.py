class ArraySet:
    
    # Constructor: sets maximum capacity of the array
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.set = [None] * capacity
        self.size = 0
    
    # Check set is empty
    # Return True if set is empty
    def isEmpty(self):
        return self.size == 0

    # Check set is full
    # Return True if set is full
    def isFull(self):
        return self.size == self.capacity

    # Return string representation of the set (only valid elements)
    def __str__(self):
        return str(self.set[0:self.size])

    # Return True if the set contains the given element, else False
    def contains(self, elem):
        for i in range(self.size):
            if self.set[i] == elem:
                return True
        return False

    # Insert element into the set if it is not full and element is not already present
    def insert(self, elem):
        if not self.isFull() and not self.contains(elem):
            self.set[self.size] = elem
            self.size += 1
        else:
            raise ValueError("Element already exists or set is full")

    # Remove the element from the set, or raise KeyError if not found
    def delete(self, elem):
        for i in range(self.size):
            if self.set[i] == elem:
                self.set[i] = self.set[self.size - 1]
                self.set[self.size - 1] = None
                self.size -= 1
                return
        raise KeyError(f"{elem} not found in set")

    # Return a new set that is the union of this set and another
    def union(self, other):
        capacity = max(self.capacity + other.capacity, self.size + other.size + 10)
        unionSet = ArraySet(capacity)
        for i in range(self.size):
            unionSet.insert(self.set[i])
        
        for i in range(other.size):
            try:
                unionSet.insert(other.set[i])
            except ValueError:
                pass
        return unionSet

    # Return a new set that is the intersection of this set and another
    def intersect(self, other):
        intersectSet = ArraySet()
        for i in range(self.size):
            if other.contains(self.set[i]):
                intersectSet.insert(self.set[i])
        return intersectSet
    
    # Return a new set that is the difference of this set and another
    def difference(self, other):
        differenceSet = ArraySet()
        for i in range(self.size):
            if not other.contains(self.set[i]):
                differenceSet.insert(self.set[i])
        return differenceSet
    

    # Returns True if all elements in this set are also in the other set
    def isSubset(self, other):
        if self.size > other.size:
            return False
        
        
        for i in range(self.size):
            check = False
            for j in range(other.size):
                if self.set[i] == other.set[j]:
                    check = True
                    break
            if check is False:
                return False
        return True

    # Returns True if both sets contain the same elements
    def isEqual(self, other):
        if self.size != other.size:
            return False
        if self.isSubset(other):
            return True
        return False

    # Empties the set
    def clear(self):
        self.set = [None] * self.capacity
        self.size = 0

    # Returns a list of the valid elements
    def toList(self):
        return list(self.set[:self.size])

    # Returns a deep copy of the set
    def copy(self):
        other = ArraySet(self.capacity)
        other.size = self.size
        for i in range(self.size):
            other.set[i] = self.set[i]
        return other
    
if __name__ == "__main__":
    print("=== ArraySet Test ===")
    
    # Create two sets
    s1 = ArraySet(5)
    s2 = ArraySet(5)

    # Insert elements
    s1.insert(1)
    s1.insert(2)
    s1.insert(3)
    print("s1:", s1)  # [1, 2, 3]

    s2.insert(3)
    s2.insert(4)
    s2.insert(5)
    print("s2:", s2)  # [3, 4, 5]

    # Test contains
    print("s1 contains 2:", s1.contains(2))  # True
    print("s2 contains 1:", s2.contains(1))  # False

    # Test delete
    s1.delete(2)
    print("s1 after deleting 2:", s1)  # [1, 3]

    # Test union
    s3 = s1.union(s2)
    print("s1 ∪ s2:", s3)  # [1, 3, 4, 5]

    # Test intersection
    s4 = s1.intersect(s2)
    print("s1 ∩ s2:", s4)  # [3]

    # Test difference
    s5 = s1.difference(s2)
    print("s1 - s2:", s5)  # [1]

    # Test isSubset
    subset = ArraySet()
    subset.insert(1)
    print("subset:", subset)
    print("subset ⊆ s1:", subset.isSubset(s1))  # True
    print("s1 ⊆ subset:", s1.isSubset(subset))  # False

    # Test isEqual
    equalSet = ArraySet()
    equalSet.insert(1)
    equalSet.insert(3)
    print("s1 == equalSet:", s1.isEqual(equalSet))  # True

    # Test clear
    s5.clear()
    print("s5 after clear():", s5)  # []

    # Test toList
    print("s1 to list:", s1.toList())  # [1, 3]

    # Test copy
    s6 = s1.copy()
    print("s6 (copy of s1):", s6)  # [1, 3]
    s6.insert(6)
    print("s1:", s1)  # [1, 3]
    print("s6 after inserting 6:", s6)  # [1, 3, 6]
