import ctypes as ct

class Node(object):
    def __init__(self, data):
        self.data = ct.py_object(data)
        self.next = None
        self.prev = None

class DoublyLinkedList(object):
    def __init__(self, dummy_node):
        self.length = 0
        self.head = Node(dummy_node)
        self.tail = self.head

    def __len__(self):
        return self.length

    def __findIndex(self, index):
        if index > (self.length//2):
            current_node = self.tail.prev
            backward_Range = self.length - index
            for _ in range(backward_Range):
                current_node = current_node.prev
        else:
            current_node = self.head.next
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
            current_node.data = ct.py_object(data)
            return current_node.data
        return current_node

    def append(self, data):
        new_node = Node(data)
        if self.length < 1:
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = self.tail
            self.tail.prev = new_node
            self.length += 1
            return new_node
        current_node = self.tail.prev
        current_node.next = new_node
        new_node.prev = current_node
        new_node.next = self.tail
        self.tail.prev = new_node
        self.length += 1
        return new_node

    def pop(self):
        if self.length < 1:
            return "Empty List!"
        current_node = self.tail.prev
        current_node.prev.next = self.tail
        self.tail.prev = current_node.prev
        self.length -= 1
        return self.tail

    def insert(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head.next
            new_node.next.prev = new_node
            self.head.next = new_node
            new_node.prev = self.head
            self.length += 1
            return new_node
        prev_index = index - 1
        prev_node = self.__findIndex(prev_index)
        # Node in front of old node, its prev is now directed to new node
        prev_node.next.prev = new_node
        # New Node next is now directed to the old node's next
        new_node.next = prev_node.next
        # Old Node's next is now directed to new node
        prev_node.next = new_node
        self.length += 1
        return new_node

    def __str__(self):
        if self.length < 1:
            return f"[{self.head.data.value}]"
        current_node = self.head
        string = "["
        for _ in range(self.length):
            string += f"{current_node.data.value}, "
            current_node = current_node.next
        string += f"{current_node.data.value}]"
        return string

if __name__ == '__main__':
    linkedlist = DoublyLinkedList("_")
    linkedlist.append("A")
    linkedlist.append("B")
    print(f"List after Append Method: {linkedlist}")
    linkedlist[0] = 1
    linkedlist[1] = 2
    print(f"List after setting index: {linkedlist}")
    linkedlist.append("C")
    linkedlist.append("D")
    linkedlist.pop()
    print(f"List after pop method: {linkedlist}")
