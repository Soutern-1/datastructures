
class Node():
    def __init__(self,value):
        self.value = value
        self.Rightchild = None
        self.Leftchild = None


root = Node(5)


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.Leftchild, key)
    else:
        root.right = insert(root.Rightchild, key)
    return root

# values = [10,20,30,40,50,60,70,80,90,100]
# for value in values:
#     insert(root,value)

def inorder(root):
    if root.Leftchild != None:
        inorder(root.Leftchild)
    print(root.value)
    if root.Rightchild !=None:
        inorder(root.Rightchild)

# def predecessor(root,key):

#     pre = None

#     while root:
#         if key <= root.value:
#             root = root.Leftchild
#         else:
#             pre = root
#             root = root.Rightchild

#     return pre

def succesor(root,key):
        

def delete(root,key):
    if root == None:
        print("root value is none; error")
    elif key < root.value:
        root.Leftchild = delete(root.Leftchild,key)
    elif key > root.value:
        root.Rightchild = delete(root.Rightchild,key)
    else:
        # if node to be replaced has only rightchild, replace
        if root.Rightchild != None and root.Leftchild == None:
            temp = root.Rightchild
            root = None
            return temp
        elif root.Righchild == None and root.Lefchild != None:
            temp = root.Leftchild
            root = None
            return temp


# Example usage
root = None
for x in [20,30,40,50,60,70,80]:
    root = insert(root, x)

key = 65
pre = predecessor(root, key)
# suc = (root, key)

print("Key:", key)
print("Predecessor:", pre.value if pre else None)
# print("Successor:", suc.key if suc else None)
