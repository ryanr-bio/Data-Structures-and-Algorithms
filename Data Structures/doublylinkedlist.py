import ctypes as ct

class Node(object):
    def __init__(self, data):
        self.data = ct.py_object(data)
        self.next = None
        self.prev = None

class DoublyLinkedList(object):
    def __init__(self):
        pass

    def __getitem__(self, index):
        pass

    def __setitem__(self, index, data):
        pass

    def append(self, data):
        pass

    def pop(self):
        pass

    def insert(self, data, index):
        pass

    def __str__(self):
        pass

if __name__ == '__main__':
    linkedlist = DoublyLinkedList()
    