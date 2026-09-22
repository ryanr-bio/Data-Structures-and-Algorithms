import ctypes

class DynamicArray(object):
    # Initialize the object with a given capacity
    def __init__(self, length):
        self.n_elemcount = 0
        self.capacity = length
        # py_object to create null pointers for capacity amount.
        self.array = (ctypes.py_object * self.capacity)()

    def __len__(self):
        # Method to return the count of elements inside the array.
        return self.n_elemcount

    def __str__(self):
        string = "["
        i = 0
        while i < (self.n_elemcount - 1):
            value = self.array[i]
            string += f"{value}, "
            i+=1
        string += f"{self.array[(self.n_elemcount - 1)]}]"
        return string 

    def __getitem__(self, index):
        # Method to return value when calling a[i]
        if index < self.n_elemcount:
            return self.array[index]
        else:
            return None

    def __setitem__(self, index, data):
        if index < self.n_elemcount:
            x = self.array[index]
        else:
            # ensures that element is only counted when setting empty pointer into value
            self.n_elemcount += 1
        self.array[index] = data
        y = self.array[index]
        return y
    
    def resize(self, n_capacity):
        new_capacity = n_capacity
        new_array = (ctypes.py_object * new_capacity)()
        index = self.n_elemcount - 1
        i = 0
        while index > 0 and i < self.n_elemcount:
            new_array[i] = self.array[i]
            i += 1
        self.array = new_array
        return self.array

    def append(self, data):
        # Method to add data to the end of the array.
        n = self.n_elemcount
        # Check if we can add given data with current capacity
        if n+1 > self.capacity:
            new_capacity = n * 2
            # if not, call resize function
            self.resize(new_capacity)
        self.array[n] = data
        self.n_elemcount += 1
        y = self.array[n]
        return y

    def remove(self, index):
        n = self.n_elemcount
        while index <= (n - 2):
            self.array[index] = self.array[(index+1)]
            index += 1
        self.n_elemcount -= 1
        self.array[(n-1)] = None
        if self.capacity >= (3 * n):
            new_capacity = self.n_elemcount // 2
            self.resize(new_capacity)
        return self.array
    
if __name__ == '__main__':
    test = DynamicArray(5)
    test[0] = "X"

    """
    This test was to check whether setting an empty space into new value
    will change the length, while also making sure changing an already existing
    value to something else would not change its length.
    """

    test[1] = "A"
    print(f"First test: {len(test)}")
    test[0] = "Y"
    print(f"Second test: {len(test)}")
    test[2] = 23
    print(f"Final test: {len(test)}")

    """
    This test was to check whether appending a value to the end of the array was
    working properly while also shifting the element count up by one.
    Also checking the print() showing up as a normal pythonic list.
    """

    test.append("Y")
    test.append("Z")
    print(f"Current Array is: {test}")
    print(f"Number of elements in this array is {len(test)}")

    """
    This test was to check whether the remove method properly adjusts the
    array index while deleting the chosen index.
    """

    test.append("Y")
    test.append("Z")
    test.append("A")
    print(test)

    test.remove(2)
    print(test)