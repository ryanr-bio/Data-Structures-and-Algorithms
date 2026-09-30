import ctypes as ct

class Node(object):
    def __init__(self, key):
        self.key = ct.py_object(key)
        self.value = None
        self.next = None

class HashTable(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = (ct.py_object * capacity)()

    def __hashCode__(self, key):
        if isinstance(key, str):
            i = 0
            sum = 0
            while i < len(key):
                sum += ord(key[i])
                i+=1
            return (sum % self.capacity)
        # Division method
        return (key % self.capacity)

    def __str__(self):
        i = 0
        length = 0
        current_node = self.array[i]
        string = "["
        while i < self.capacity:
            print(f" total length = {self.length}")
            print(length)
            if not current_node:
                try:
                    i += 1
                    current_node = self.array[i]
                except:
                    continue
            if current_node.key.value != 'head' and length < self.length - 1:
                string += f"{current_node.key.value}: {current_node.value.value}, \n"
                length += 1
                current_node = current_node.next
            elif current_node.key.value != 'head':
                string += f"{current_node.key.value}: {current_node.value.value}"
                length += 1
                current_node = current_node.next
            else:
                current_node = current_node.next
        string += "]"
        return string

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        index = self.__hashCode__(key)
        current_node = self.array[index]

        while current_node.next:
            if current_node.key.value == key:
                return current_node.value.value
            current_node = current_node.next
        return None

    def __setitem__(self, key, value):
        index = self.__hashCode__(key)
        try:
            self.array[index]
        except:
            self.array[index] = Node('head')
        current_node = self.array[index]

        while current_node.next:
            if current_node.key.value == key:
                current_node.value = ct.py_object(value)
                return current_node.value.value
            current_node = current_node.next
        new_node = Node(key)
        new_node.value = ct.py_object(value)
        new_node.next = None
        current_node.next = new_node
        self.length += 1
        return new_node

    def delete(self, key):
        index = self.__hashCode__(key)
        current_node = self.array[index]
        
        while current_node.next:
            if current_node.next.key.value == key:
                current_node.next = current_node.next.next
                return current_node
            current_node = current_node.next
        return "Key does not exist!"

if __name__ == '__main__':
    dict = HashTable(5)
    dict["Ryan"] = 3.8
    dict["Eram"] = 4.0
    print(dict)