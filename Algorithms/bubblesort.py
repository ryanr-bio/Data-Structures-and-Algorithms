import random

def BubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            else:
                continue
    return array

if __name__ == '__main__':
    pool = range(100)
    array = random.sample(pool, 10)
    print(array)
    sorted_array = BubbleSort(array)
    print(sorted_array)