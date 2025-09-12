

class Stack():
    def __init__(self):
        self.stack = []
        self.top = 0
        self.max_stack = 5
    def push(self,item_to_append):
        if self.top<self.max_stack:
            self.stack.append(item_to_append)
            self.top = len(self.stack)
            # print(f"Item {item_to_append} added to stack at position {self.top-1}")
        else:
            print("Stack Overflow")
    def pop(self):
        if self.top != 0:
            temp = self.stack.pop()
            self.top-=1
            # print(f"Item {temp} successfully removed from stack ")

        else:
            print("Stack Underflow")

    # def info(self):
    #     print(f"Top: {self.top}" )
    #     print(self.stack)

text = Stack()
undo = Stack()
redo = Stack()

def main():
    print("--------------------------")
    print("Options: Undo, Redo, Add, View")
    action = input("What action would you like to perform: ")
    if action == "undo":
        undo.push(text.stack[-1])
        text.pop()

        print("Undid last addition! Current text is:")
        print(text.stack)
        main()
    if action == "redo" :
        text.push(undo.stack[-1])
        undo.pop()
        print("Undid the undo! Current text is:")
        print(text.stack)
        main()
    if action == "add":
        inp = str(input("Enter the string you want to add: "))
        text.push(inp)
        
        # undo.push(str)
        print(undo.stack)
        print("Added string to stack! Current text is:")
        print(text.stack)
        main()
    if action == "view":
        print(text.stack)
        main()
    else:
        "Enter valid input"

        main()

undo.push(" ")
main()
