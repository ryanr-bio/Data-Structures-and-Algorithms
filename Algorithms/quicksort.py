import random
def quickSort(array, start, end):
    if  start >= end:
        return array
    i = start
    j = start - 1
    pivot = end - 1
    for i in range(start, end-1):
        if array[i] < array[pivot]:
            j += 1
            array[j], array[i] = array[i], array[j]
    
    array[j+1], array[pivot] = array[pivot], array[j+1]

    quickSort(array, start, j+1)
    quickSort(array, j + 2, end)
    return array

if __name__ == '__main__':
    array = random.sample(range(10), 10)
    print(f"Unsorted Array: {array}")
    sorted_array = quickSort(array, 0, len(array))

    print(f"Sorted Array: {sorted_array}")

