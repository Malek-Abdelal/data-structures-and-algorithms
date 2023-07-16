## Insertion Sort:

Insertion Sort is a simple sorting algorithm that builds the final sorted array one element at a time. It is efficient for small data sets or nearly sorted arrays. The algorithm works as follows:

1. The `insert` function takes a sorted array (`sorted_array`) and a value to be inserted (`value`).
2. It initializes `i` to 0 and iterates while `i` is less than the length of `sorted_array` and `value` is greater than the element at index `i` in `sorted_array`.
3. It increments `i` by 1 until the condition is no longer satisfied, finding the correct position to insert `value`.
4. It inserts `value` at index `i` in `sorted_array`.
Insertion Sort Algorithm Visualization:

```python
def insert(sorted_array, value):
    i = 0
    while i < len(sorted_array) and value > sorted_array[i]:
        i += 1
    sorted_array.insert(i, value)

def insertion_sort(input):
    sorted_array = [input[0]]  # Create an empty sorted array and add the first element of input to it.
    for num in input[1:]:  # Iterate over the remaining elements of input from index 1 to the end.
        insert(sorted_array, num)  # Call the insert function to insert the element into the sorted array.
    return sorted_array  # Return the sorted array as the sorted result.
```

**Example:**

```python
sorted_result = insertion_sort([5, 2, 4, 6, 1, 3])
print(sorted_result)  # Output: [1, 2, 3, 4, 5, 6]
```

**Efficiency:**

**Time Complexity:** The `insert` function takes O(n) time to find the correct position to insert the value, and the `insertion_sort` function calls `insert` for each element in the input, resulting in an overall time complexity of O(n^2).
**Space Complexity:** The `insert` function operates in-place, using O(1) space, and the `insertion_sort` function creates a new sorted array, resulting in a space complexity of O(n).

Insertion Sort is best suited for small datasets or situations where the array is almost sorted, as its time complexity can become inefficient for larger arrays.
