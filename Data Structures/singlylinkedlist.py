import ctypes

class Node(object):
    def __init__(self, data):
        self.data = ctypes.py_object(data)
        self.next = None

class SinglyLinkedList(object):

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.length

    def append(self, data):
        if self.head  == None and self.tail == None:
            self.head = Node(data)
            self.tail = self.head
            self.length += 1
            return self.tail
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        new_node = Node(data)
        current_node.next = new_node
        self.tail = new_node
        self.length += 1
        return self.tail

    def pop(self):
        if self.head == None:
            return "Empty List"
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return self
        current_node = self.head
        for _ in range(self.length - 2):
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node
        self.length -= 1
        return current_node

    def __findIndex(self, index):
        #Not sure if negative indexing needs to be added for linkedlists.
        if (self.length - 1) < index:
            return "Index is out of list length!"
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    def __getitem__(self, index):
        current_node = self.__findIndex(index)
        if type(current_node) == Node:
            return current_node.data.value
        return current_node
    
    def __setitem__(self, index, data):
        current_node = self.__findIndex(index)
        if type(current_node) == Node:
            current_node.data = ctypes.py_object(data)
            return current_node.data
        return current_node

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return new_node
        prev_index = index - 1
        prev_node = self.__findIndex(prev_index)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1
        return new_node

    def __str__(self):
        if self.head == None:
            return "[]"
        current_node = self.head
        string = "["
        while current_node.next != None:
            string += f"{current_node.data.value}, "
            current_node = current_node.next
        string += f"{current_node.data.value}]"
        return string

if __name__ == '__main__':
    linkedList = SinglyLinkedList()
    linkedList.append(0)
    linkedList.append(1)
    linkedList.append(2)
    print(f"List after appending: {linkedList}")
    linkedList.pop()
    print(f"List after popping: {linkedList}")
    print(f"Node at Index 0: {linkedList[0]}")
    print(f"Node at Index 2: {linkedList[2]}")
    linkedList[0] = "A"
    print(f"Node at index 0 is set to: {linkedList[0]}")
    linkedList.insert(0, "Z")
    print(f"Insertion at 0 index: {linkedList}")
    linkedList.insert(2, "B")
    print(f"Insertion at index 2: {linkedList}")