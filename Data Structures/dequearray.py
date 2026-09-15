import ctypes

class DequeArray(object):
    def __init__(self, length):
        self.n_elemcount = 0
        self.j_tracker = 0
        self.capacity = length
        self.array = (ctypes.py_object * self.capacity)()

    def __len__(self):
        return self.n_elemcount

    def __str__(self):
        string = "["
        i = 0
        if self.n_elemcount < 1:
            return "[]"
        while i < (self.n_elemcount - 1):
            value = self.array[(self.j_tracker + i)% self.capacity]
            string += f"{value}, "
            i+=1
        string += f"{self.array[(self.j_tracker + i)% self.capacity]}]"
        return string 
        
    def __getitem__(self, index):
        return self.array[(index + self.j_tracker) % self.capacity]

    def __setitem__(self, index, data):
        self.array[index] = data
        y = self.array[index]
        if (index > (self.n_elemcount - 1)):
            self.n_elemcount += 1
        return y 

    def resize(self, n_capacity):
        new_capacity = n_capacity
        new_array = (ctypes.py_object * new_capacity)()
        index = self.n_elemcount - 1
        for i in range(index):
            new_array[i] = self.array[i]
        self.array = new_array
        return self.array

    def add(self, index, data):
        n = self.n_elemcount
        j = self.j_tracker
        if n + 1 > self.capacity:
            n_capacity = (self.capacity * 2)
            self.resize(n_capacity)
        if index < (n/2):
            j = ((j + index) % self.capacity)
            for k in range(index):
                self.array[(j + k) % self.capacity] = self.array[(j + k + 1) % self.capacity]
        else:
            for k in range(n, (index + 1), -1):
                self.array[(j + k) % self.capacity] = self.array[(j + k - 1) % self.capacity]
        self.array[(j + index) % self.capacity] = data
        self.n_elemcount += 1
        return data

    def remove(self, index):
        n = self.n_elemcount
        j = self.j_tracker
        if index < (n/2):
            for k in range(index, 1, -1):
                self.array[(j+k) % self.capacity] = self.array[(j+k-1) % self.capacity]
            j = ((j + index) % self.capacity)
        else:
            for k in range(index, n - 2):
                self.array[(j+k) % self.capacity] = self.array[(j+k+1) % self.capacity]
        self.n_elemcount -= 1
        if 3*n <= self.capacity:
            n_capacity = self.capacity // 2
            self.resize(n_capacity) 
        return self.array

if __name__ == '__main__':
    test = DequeArray(5)
    test.add(index=0, data=2)
    test.add(index=1, data= 6)
    test.remove(1)
    print(test)