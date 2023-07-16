## Merge Sort:

Merge Sort is an efficient sorting algorithm that divides the input array into smaller halves, recursively sorts them, and then merges them back to produce the final sorted array.

**mergesort function:**

The `mergesort` function takes an array as input and performs the following steps:

1. Check the length of the array.
2. If the length is greater than 1, calculate the midpoint (mid) of the array.
3. Divide the array into two halves: left (from index 0 to mid-1) and right (from index mid to the end).
4. Recursively call mergesort on the left and right halves.
5. Finally, merge the sorted left and right halves using the merge function.

**merge function:**

The `merge` function takes three arrays as input: left, right, and arr. It performs the following steps:

1. Initialize three pointers i, j, and k to keep track of the indices in left, right, and arr, respectively.
2. Compare elements from the left and right arrays and place the smaller element in arr at index k.
3. Update the pointers i, j, and k accordingly.
4. After the above loop, if there are any remaining elements in either the left or right array, they are appended to arr.

**Visualization:**

Below is an example visualization of the Merge Sort process:

```python
[4, 2, 1, 5, 3]              # Initial unsorted array
        /    \
[4, 2]            [1, 5, 3]    # Splitting into halves
  /    \          /    \
[4]    [2]      [1]    [5, 3]   # Splitting further
 |      |       |    /   \
[2, 4]  [1]     [1, 3]  [5]     # Merging back sorted halves
     \    /          \
  [1, 2, 4]         [1, 3, 5]   # Final merge of left and right halves
       \              /
[1, 1, 2, 3, 4, 5]            # Sorted array
```

**Efficiency:**

**Time Complexity:** The time complexity of Merge Sort is O(n log n), where n is the number of elements in the input array.
**Space Complexity:** The space complexity of Merge Sort is O(n), where n is the number of elements in the input array. This is because the algorithm uses additional space for temporary arrays during the merge process.

