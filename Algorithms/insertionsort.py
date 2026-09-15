import random

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0:
            if array[j] > key:
                array[j + 1] = array[j]
                i = j
            j -= 1
        array[i] = key
    return array

if __name__ == '__main__':
    array = random.sample(range(10), 10)
    print(f"Unsorted array: {array}")
    sorted_array = insertionSort(array)
    print(f"Sorted Array: {sorted_array}")
