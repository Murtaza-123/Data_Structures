#Create a class
class Node:
#Construct a new Node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#Inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(
        root.key),
        inorder(root.right)

#Insert a nodes
def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node




#Deletion Case1
def minValueNode(node):
    current = node

    while (current.left is not None):
        current = current.left

    return current




#delete a leaf node Recursively
def deleteNode(root, key):
    if root is None:
        return root


    if key < root.key:
        root.left = deleteNode(root.left, key)

    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    #Case2 delete a node with one child or not child
    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        #node with two children


        temp = minValueNode(root.right)


        root.key = temp.key

        root.right = deleteNode(root.right, temp.key)

    return root
#Searching in BST
def search(root, key):
    if root is None or root.key == key:
        return root

    if root.key < key:
        return search(root.right, key)

    return search(root.left, key)



#Driver code
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
root = search(root,30)
print(
"Inorder traversal of the given tree")
inorder(root)

print(
"\nDelete 20")
root = deleteNode(root, 20)
print(
"Inorder traversal of the modified tree")
inorder(root)

print(
"\nDelete 30")
root = deleteNode(root, 30)
print(
"Inorder traversal of the modified tree")
inorder(root)

print(
"\nDelete 50")
root = deleteNode(root, 50)
print(
"Inorder traversal of the modified tree")
inorder(root)

