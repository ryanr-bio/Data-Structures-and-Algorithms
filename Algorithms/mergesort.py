import random

def mergeSort(array):
    length = len(array)
    if length <= 1:
        return array
    mid = length//2
    leftarray = list()
    rightarray = list()
    for i in range(length):
        if i < mid:
            leftarray.append(array[i])
        else:
            rightarray.append(array[i])
    leftarray = mergeSort(leftarray)
    rightarray = mergeSort(rightarray)

    merge(leftarray, rightarray, array) 
    return array
def merge(left, right, original):
    leftsize  = len(original) // 2
    rightsize = len(original) - leftsize
    l = 0
    r = 0
    i = 0
    while l < leftsize and r < rightsize and i < len(original):
        if left[l] < right[r]:
            original[i] = left[l]
            l+=1
            
        elif right[r] < left[l]:
            original[i] = right[r]
            r+=1
        i+=1
    while l < leftsize:
        original[i] = left[l]
        l += 1
        i += 1
    while r < rightsize:
        original[i] = right[r]
        r += 1
        i += 1
    return original

if __name__ == '__main__':
    array = random.sample(range(10),10)
    print(array)
    sorted_array = mergeSort(array)
    print(f"Sorted Array is: {sorted_array}")