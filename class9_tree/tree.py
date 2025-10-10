class Node():
    def __init__(self,value):
        self.value = value
        self.Rightchild = None
        self.Leftchild = None

root = Node(2)
root.Rightchild = Node(3)
root.Leftchild = Node(4)

root.Leftchild.Leftchild = Node(5)
root.Leftchild.Rightchild = Node(6)

root.Rightchild.Leftchild = Node(7)
root.Rightchild.Rightchild = Node(8)

root.Leftchild.Rightchild.Rightchild = Node(9)


#  Inorder Traversal
# Cover entire left tree from left section
# Then cover root / parent
# Then cover entire right side

# preorder
# start with root
# left -> right
# 

# postorder
# left -> right
# root



def inorder(root):
    if root.Leftchild != None:
        inorder(root.Leftchild)
    print(root.value)
    if root.Rightchild !=None:
        inorder(root.Rightchild)

inorder(root)
    




