class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        newNode = node(data)
        self.tail = newNode
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current

    def display_f(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next

    def display_b(self):
        current = self.tail
        while current:
            print(current.data, end="<-")
            current = current.prev


obj = linkedlist()
obj.insert(5)
obj.insert(6)
obj.insert(3)
obj.display_f()
obj.display_b()