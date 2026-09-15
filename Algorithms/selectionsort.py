import random

def SelectionSort(array: object):
    for i in range((len(array) - 1)):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                min = j
            else:
                continue
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
        print(f"This is {i} iteration: {array}")
    return array

if __name__ == '__main__':
    array = random.sample(range(10), 10)
    print(array)
    sorted_array = SelectionSort(array)
    print(sorted_array)
