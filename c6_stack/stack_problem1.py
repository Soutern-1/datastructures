# Write a python program to find whether a given string has balanced parentheses or not.

string = "[{12[3(13,3])4}]"


class Stack():
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self,item_to_append):
        self.stack.append(item_to_append)
        if self.stack[-1] == "Right_Curly" and self.stack[-2] == "Left_Curly":
            print("Detected One set of { }")
            self.stack.pop()
            self.stack.pop()
        elif self.stack[self.top] == "Right_Rounded" and self.stack[self.top-1] == "Left_Rounded":
            print("Detected One set of ( )")
            self.stack.pop()
            self.stack.pop()
        elif self.stack[self.top] == "Right_Square" and self.stack[self.top-1] == "Left_Square":
            print("Detected One set of [ ]")
            self.stack.pop()
            self.stack.pop()
            if len(self.stack) > 2:
                if self.stack[self.top] == ("Right_Square" or "Right_Rounded" or "Right_Curly") and self.stack[self.top-1] == ("Right_Square" or "Right_Rounded" or "Right_Curly"):
                    pass
                elif self.stack[self.top] == ("Left_Square" or "Left_Rounded" or "Left_Curly") and self.stack[self.top-1] == ("Left_Square" or "Left_Rounded" or "Left_Curly"):
                    pass
                else:
                    print("Error: Mismatched parentheses closed")
                    print(f"{self.stack[-1]} and {self.stack[-2]} are not matching pairs")
        

        self.top = len(self.stack)


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

for i in string:
    if i == "[":
        stack.push("Left_Square")
    if i == "{":
        stack.push("Left_Curly")
    if i == "(":
        stack.push("Left_Rounded")
    if i == "]":
        stack.push("Right_Square")
    if i =="}":
        stack.push("Right_Curly")
    if i == ")":
        stack.push("Right_Rounded")

if stack.top > 0:
    print("Not all parentheses have a pair")
    stack.info()