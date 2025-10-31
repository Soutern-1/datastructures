
class Node():
    def __init__(self,value):
        self.value = value
        self.Rightchild = None
        self.Leftchild = None


root = Node(1)
root.Rightchild = Node(3)
root.Leftchild = Node(2)

root.Leftchild.Leftchild = Node(4)
root.Leftchild.Rightchild = Node(5)

root.Rightchild.Leftchild = Node(6)
root.Rightchild.Rightchild = Node(7)

search_value = int(input("What value do you want to search for: "))

flag = False

def search(root,search_value):
    global flag
    if root.value == search_value:
        print("Value found in tree")
        flag = True
    else:
        if root.Leftchild != None:
            search(root.Leftchild, search_value)
        elif root.Rightchild != None:
            search(root.Rightchild, search_value)


search(root,search_value)


if flag == False:
    print("Value not found in tree")