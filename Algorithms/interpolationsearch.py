def interpolation(array: object, target: int):
    low = 0
    high = (len(array) - 1)
    while (target >= array[low]) and (target <= array[high]) and (low <= high):
        probe = low + (high - low) * (target - array[low]) // (array[high] - array[low])
        if array[probe] < target:
            low = probe + 1
        elif array[probe] > target:
            high = probe - 1
        else:
            return probe
    return -1

if __name__ == '__main__':
    array = [i for i in range(0, 200, 5)]

    test = interpolation(array, 20)
    print(test)