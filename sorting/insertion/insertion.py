def insert(sorted_array, value):
    i = 0
    while i < len(sorted_array) and value > sorted_array[i]:
        i += 1
    sorted_array.insert(i, value)

def insertion_sort(input_list):
    sorted_list = [input_list[0]]  # Create an empty sorted list and add the first element of input to it.
    for num in input_list[1:]:  # Iterate over the remaining elements of input from index 1 to the end.
        insert(sorted_list, num)  # Call the insert function to insert the element into the sorted list.
    return sorted_list  # Return the sorted list as the sorted result.
