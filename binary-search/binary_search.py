array = [3, 4, 5, 6, 7, 8, 9]
x = 10

def BinarySearch(array, x):

    low = 0
    high = len(array)-1

    while low <= high:
            mid = low + (high - low)//2
            if array[mid] == x:
                return mid
            elif array[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

    return -1

print(BinarySearch(array, x))