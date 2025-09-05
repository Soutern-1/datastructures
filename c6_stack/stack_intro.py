

class Stack():
    def __init__(self):
        self.stack = []
        self.top = 0
        self.max_stack = 5
    def push(self,item_to_append):
        if self.top<self.max_stack:
            self.stack.append(item_to_append)
            self.top = len(self.stack)
            print(f"Item {item_to_append} added to stack at position {self.top-1}")
        else:
            print("Stack Overflow")
    def pop(self):
        if self.top != 1:
            temp = self.stack.pop()
            self.top-=1
            print(f"Item {temp} successfully removed from stack ")

        else:
            print("Stack Underflow")

    def info(self):
        print(f"Top: {self.top}" )
        print(self.stack)

stack = Stack()

stack.push(6)
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

stack.info()

stack.pop()

stack.info()


