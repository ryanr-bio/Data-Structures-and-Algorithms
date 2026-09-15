def BinarySearch(array: object, target: int):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = low + (high - low) // 2
        mid_val = array[middle]
        if mid_val < target:
            low = middle + 1
        elif mid_val > target:
            high = middle - 1
        else:
            return middle
    return -1

if __name__ == '__main__':
    # Array to search through has to be a sorted array.
    array = [i for i in range(1000, 5000)]

    target_index = BinarySearch(array, 2000)
    print(target_index)