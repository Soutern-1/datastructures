# get an input value

# 1st value becomes our root
# get another value

# function
# if value < root
# make value the left node
# function(input, left node)
# if value > root
# make value the right node
# function(input, right node)
# if left and right == None

# if number is duplicate check  to the right node and add if from there

class Node():
    def __init__(self,value):
        self.value = value
        self.Rightchild = None
        self.Leftchild = None

def insert_child(root,data):
    if int(data) < int(root.value) and root.Leftchild == None:
        root.Leftchild = Node(data)
    elif data < root.value and root.Leftchild !=None:
        insert_child(root.Leftchild,data)
    elif data > root.value and root.Leftchild == None:
        root.Leftchild = Node(data)
    elif data < root.value and root.Leftchild != None:
        insert_child(root.Rightchild, data)
    elif data == root:
        print("The value was equal to the root, defaulting to right")
        insert_child(root.Rightchild,data)
    else:
        print("Error, did not pass any of the if statements")


def inorder(root):
    if root.Leftchild != None:
        inorder(root.Leftchild)
    print(root.value)
    if root.Rightchild !=None:
        inorder(root.Rightchild)

def main():
    choice = input(("Enter choice:Add / view: "))
    if choice == "add":
        value = int(input("Enter value of node: "))
        insert_child(root, value)
        main()
    elif choice == "view":
        inorder(root)
        main()
    else:
        print("Make a valid choice")
        main()


    
value = int(input("Enter value of root node: "))
root = Node(value)

main()


