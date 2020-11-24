import random
from binarytree import tree, bst, heap

class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None

def insertLevelOrder(arr, root, i, n): 
    if i < n: 
        temp = newNode(arr[i])  
        root = temp  
        root.left = insertLevelOrder(arr, root.left,2 * i + 1, n)  

        root.right = insertLevelOrder(arr, root.right,2 * i + 2, n) 
    return root 

def ranGen(n):
    randomlist = []
    for i in range(0,n):
        key = random.randint(1,99)
        randomlist.append(key)
    return randomlist
