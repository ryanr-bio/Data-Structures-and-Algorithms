import ctypes

class QueueArray(object):
    def __init__(self, length):
        self.n_elemcount = 0
        # j keeps track of where a[0] is at all times in the looped array
        self.j_position = 0
        self.capacity = length
        self.array = (ctypes.py_object * self.capacity)()
    
    def __len__(self):
        return self.n_elemcount
    
    def __str__(self):
        string = "["
        i = 0
        while i < (self.n_elemcount - 1):
            value = self.array[(self.j_position + i) % self.capacity]
            string += f"{value}, "
            i+=1
        string += f"{self.array[(self.j_position + i) % self.capacity]}]"
        return string 
    
    def __getitem__(self, index):
        return self.array[(self.j_position + index) % self.capacity]
        
    def resize(self, n_capacity):
        new_capacity = n_capacity
        new_array = (ctypes.py_object * new_capacity)()
        index = self.n_elemcount
        for i in range(index):
            new_array[i] = self.array[(self.j_position + i) % self.capacity]
        self.array = new_array
        self.j_position = 0
        return self.array
    
    def enqueue(self, data):
        n = self.n_elemcount
        if n+1 > self.capacity:
            new_capacity = n * 2
            self.resize(new_capacity)
        self.array[(self.j_position+n) % self.capacity] = data
        self.n_elemcount += 1
        return data
    
    def dequeue(self):
        y = self.array[self.j_position]
        self.j_position = (self.j_position + 1) % self.capacity
        self.n_elemcount -= 1
        
        if self.capacity >= (3 * self.n_elemcount):
            new_capacity = self.n_elemcount // 2
            self.resize(new_capacity)
        return y

if __name__ == '__main__':
    queue = QueueArray(5)
    for i in range(5):
        queue.enqueue(i)
    
    print(f"Filled Queue : {queue}")
    queue.dequeue()
    print(f"Queue after first pop: {queue}")
    queue.dequeue()
    print(f"Queue after second pop: {queue}")
    print(queue[1])