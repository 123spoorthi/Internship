class stack:
    def _init_(self):
        self.stack = []
        self.size = 5
        self.top = -1
    def push(self, item):
        if self.top < self.size:
            self.stack.append(item)
            self.top += 1
        else:
            print("Stack is full")
    def display(self):
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i])
    def pop(self):
        if len(self.stack) == 0:
            print("underflow")
        else:
            self.stack.pop()
    def  isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
obj=stack()
obj.push("apple")
obj.push("banana")
obj.push("cherry")
obj.push("pear")
obj.push("mango")
obj.push("kiwi")
obj.push("orange")
obj.push("strawberry")
obj.pop()
obj.display()