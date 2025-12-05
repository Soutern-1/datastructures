
# Class
class Node():
    def __init__(self,value):
        self.value = value
        self.Rightchild = None
        self.Leftchild = None

# Insert function
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.Leftchild = insert(root.Leftchild, key)
    else:
        root.Rightchild = insert(root.Rightchild, key)
    # print("Value added")
    return root


def inorder(root):
    if root:
        inorder(root.Leftchild)
        print(root.value,end=" ")
        # pint("value printed")
        inorder(root.Rightchild)


def delete(root,del_value):
    if root is None:
        return root
    # Search for the node that is to be deleted
    if del_value < root.value:
        root.left = delete(root.Leftchild, del_value)
    elif del_value > root.value:
        root.right = delete(root.Rightchild,del_value)
    else:
        # root value = del_value - node to be deleted is found
        if root.Leftchild == None and root.Rightchild == None:
            return None
        elif root.Leftchild != None and root.Righthild == None:
            return root.Leftchild
        elif root.Rightchild != None and root.Leftchild == None:
            return root.Rightchild
        else:
            temp = root.Rightchild
            while temp.Leftchild:
                temp = root.Leftchild
            root.value = temp.value
            root.rightchild = delete(root.Rightchild, temp.value)
    return root


root = Node(50)

list = [49,5,56,92,30,55,10,99,65,40,33,83,70,22]
for x in list:
    root = insert(root,x)

print(root.Leftchild.Leftchild.value)
inorder(root)
new_root = delete(root, int(input("What value should be deleted?: ")))
inorder(new_root)

# ---------------------------------------------

