# Singly Linked List Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """List-er shesh e notun node add kora"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """List-er shuru te notun node add kora"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head
        prev = None
        if current and current.data == key:
            self.head = current.next
            return
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next

    def traverse(self):
        element = []
        current = self.head
        while current:
            element.append(current.data)
            current = current.next
        return element

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    
l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)

l.reverse()
print(l.traverse())