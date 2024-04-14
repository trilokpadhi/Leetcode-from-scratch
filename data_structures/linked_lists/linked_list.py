class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self.head
    
    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            return
        while current:
            if current.data == data:
                break
            prev = current
            current = current.next
        prev.next = current.next
        return self.head
    
    def insert(self, index, data):
        new_node = Node(data)
        current = self.head
        if index == 0:
            self.head = new_node
            new_node.next = current
            return
        for i in range(index-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return self.head
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        return self.head
    
