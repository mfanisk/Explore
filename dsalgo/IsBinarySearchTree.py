from dsalgo.BinaryTree import node

INT_MAX = 4294967296
INT_MIN = -4294967296

def checkBST(root):
       return checkBSTUtil(root,INT_MIN,INT_MAX)

def checkBSTUtil(node,min,max):
    if node is None:
        return True
    if node.data > max or node.data < min:
        return False
    return checkBSTUtil(node.left,min,node.data-1) and checkBSTUtil(node.right,node.data + 1, max)