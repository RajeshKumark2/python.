class Tree:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

def insert(root, key):
    if not root:
        return Tree(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

root = None 
root = insert(root, 50)
insert(root, 30)
insert(root, 70) 


        