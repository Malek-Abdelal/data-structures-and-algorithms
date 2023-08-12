# Hash Tables Implementation

Implementing Hash tables with it's methods **(get, set, __hash, has, keys)**.

## The time and space complexity for each method:

**1. __hash(self, key):**

**Time Complexity:** O(k), where k is the length of the key.

**Space Complexity:** O(1)

**2. set(self, key, value):**

**Time Complexity:** O(1) on average. In the worst case (hash collisions), it can be up to O(n), where n is the number of elements in the same bucket.

**Space Complexity:** O(1)

**3. get(self, key):**

**Time Complexity:** O(1) on average. In the worst case (hash collisions), it can be up to O(n), where n is the number of elements in the same bucket.

**Space Complexity:** O(1)

**4. has(self, key):**

**Time Complexity:** O(1) on average. In the worst case (hash collisions), it can be up to O(n), where n is the number of elements in the same bucket.

**Space Complexity:** O(1)

**5. keys(self):**

**Time Complexity:** O(1)

**Space Complexity:** O(n), where n is the number of key-value pairs in the HashTable. The method stores all the keys in the keys_list.