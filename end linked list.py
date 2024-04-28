class node:
    def _init_(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def _init_(self):
        self.head=None
    def insert_at_end(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newNode

    def insert_at_beginning(self,data):
         NewNode=node(data)
         if self.head is None:
            self.head=NewNode
         else:
            NewNode.next=self.head
            self.head=NewNode
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
    def insert_at_position(self,data,position):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        elif pos