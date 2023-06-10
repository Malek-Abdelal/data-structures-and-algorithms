import math
array = [1, 2, 3, 4, 5]
value = 10

def insertShiftArray(arr, value):
    mid_index = math.ceil((len(arr) / 2))
    new_list = arr[:mid_index] + [value] + arr[mid_index:]
    return new_list 

print(insertShiftArray(array, value))