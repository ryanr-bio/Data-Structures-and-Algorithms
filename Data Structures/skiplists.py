import random as rand
import ctypes as ct
from dynamicarray import DynamicArray
'''
This skiplist class is made for a sorted set.
'''
class Node(object):

    def __init__(self, data, height):
        self.data = ct.py_object(data)
        self.height = height
        #New attribute for node to keep track of which layer we are on.
        self.array = DynamicArray(height + 1)

class SkipListSSet(object):

    def __init__(self, maxheight):
        self.maxheight = maxheight
        self.length = 0
        self.sentinel = Node('sentinel', self.maxheight)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        i = 0
        current_node = self.sentinel
        while i < self.length:
            if i == index:
                return current_node.array[0].data.value
            current_node = current_node.array[0]
            i += 1
        return "{index} is out of index."

    def __searchpath(self, data):
        current_node = self.sentinel
        for i in range(self.maxheight + 1, -1, -1):
            while current_node.array[i] != None and current_node.array[i].data.value < data:
                current_node = current_node.array[i]
        return current_node
    
    def pick_height(self, max_height):
        z = rand.getrandbits(32)
        k = 0
        while (z & 1) and k < max_height + 1:
            k += 1
            z = z//2
        return k
    
    def add(self, data):
        prev_node = self.__searchpath(data)
        if prev_node.array[0] != None and prev_node.array[0].data.value == data:
            print("Item already in sorted set!")
            return
        new_node = Node(data, self.pick_height(self.maxheight))
        new_node.array[0] = prev_node.array[0]
        prev_node.array[0] = new_node
        for i in range(1, new_node.height + 1):
            current_node = self.sentinel
            while current_node.array[i] != None and current_node.array[i].data.value < data:
                current_node = current_node.array[i]
            new_node.array[i] = current_node.array[i]
            current_node.array[i] = new_node
        self.length += 1
        return new_node
             
    def remove(self, data):
        prev_node = self.__searchpath(data)
        if prev_node.array[0] == None or prev_node.array[0].data.value != data:
            print("Item not found!")
            return
        height = prev_node.array[0].height
        prev_node.array[0] = prev_node.array[0].array[0]
        for i in range(1, height + 1):
            current_node = self.sentinel
            while current_node.array[i] != None and current_node.array[i].data.value < data:
                current_node = current_node.array[i]
            current_node.array[i] = current_node.array[i].array[i]
        self.length -= 1
        return 
            
    
    def __str__(self):
        current_node = self.sentinel
        string = "["
        i = 0
        while current_node.array[0] != None:
            current_node = current_node.array[0]
            string += f"{current_node.data.value}"
            if i < self.length - 1:
                string += ", "
            i += 1            
        string += "]"
        return string
    
if __name__ == '__main__':
    skiplist = SkipListSSet(32)
    skiplist.add(0)
    skiplist.add(5)
    skiplist.add(3)
    skiplist.add(2)
    skiplist.add(0) # Testing statement for detecting repeating data.
    print(f"Sorted Set after addition: {skiplist}")
    print(f"3rd element is {skiplist[2]}")
    skiplist.remove(3)
    skiplist.remove(5)
    skiplist.remove(7) # Testing statement for avoiding wrong removal request.
    print(f"Sorted Set after removal: {skiplist}")
    print(f"2nd element is {skiplist[1]}")