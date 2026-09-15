import ctypes

class StackArray(object):
    def __init__(self, length):
        self.n_elemcount = 0
        self.capacity = length
        self.array = (ctypes.py_object * self.capacity)()
    
    def __len__(self):
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
        return self.array[index]
        
    def resize(self, n_capacity):
        new_capacity = n_capacity
        new_array = (ctypes.py_object * new_capacity)()
        index = self.n_elemcount - 1
        for i in range(index):
            new_array[i] = self.array[i]
        self.array = new_array
        return self.array
    
    def push(self, data):
        n = self.n_elemcount
        if n+1 > self.capacity:
            new_capacity = self.n_elemcount * 2
            self.resize(new_capacity)
        self.array[n] = data
        self.n_elemcount += 1
        y = self.array[n]
        return y
    
    def pop(self):
        n = self.n_elemcount
        self.n_elemcount -= 1
        self.array[(n-1)] = None
        if self.capacity >= (3 * n):
            new_capacity = self.n_elemcount / 2
            self.resize(new_capacity)
        return self.array

if __name__ == '__main__':
    stack = StackArray(5)
    for i in range(5):
        stack.push(i)
    
    print(f"Filled Stack : {stack}")
    stack.pop()
    print(f"Stack after first pop: {stack}")
    stack.pop()
    print(f"Stack after second pop: {stack}")
    print(stack[1])