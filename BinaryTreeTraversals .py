import pylab
import time
import myLibrary as lib

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

# Computes recursively the height of a binary tree
# Input: A binary tree T
# Output: The height of T
def Height(root):
	if root is None:
		return -1
	return max(Height(root.left), Height(root.right))+1

# A = [22, 20, 88, 84, 65, 10, 4, 75, 68, 6]
# print(Height(A))
# #3

A0 = lib.ranGen(10)
A1 = lib.ranGen(1000)
A2 = lib.ranGen(2000)
A3 = lib.ranGen(3000)
A4 = lib.ranGen(4000)
A5 = lib.ranGen(5000)
A6 = lib.ranGen(6000)
A7 = lib.ranGen(7000)
A8 = lib.ranGen(8000)
A9 = lib.ranGen(9000)

root0 = None
root0 = insertLevelOrder(A0, root0, 0, len(A0) )
root1 = None
root1 = insertLevelOrder(A1, root1, 0, len(A1) )
root2 = None
root2 = insertLevelOrder(A2, root2, 0, len(A2) )
root3 = None
root3 = insertLevelOrder(A3, root3, 0, len(A3) )
root4 = None
root4 = insertLevelOrder(A4, root4, 0, len(A4) )
root5 = None
root5 = insertLevelOrder(A5, root5, 0, len(A5) )
root6 = None
root6 = insertLevelOrder(A6, root6, 0, len(A6) )
root7 = None
root7 = insertLevelOrder(A7, root7, 0, len(A7) )
root8 = None
root8 = insertLevelOrder(A8, root8, 0, len(A8) )
root9 = None
root9 = insertLevelOrder(A9, root9, 0, len(A9) )

#0
startA0 = time.time()
print(Height(root0))
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(A0)
print(A0)
#1
startA1 = time.time()
print(Height(root1))
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(A1)
#2
startA2 = time.time()
print(Height(root2))
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(A2)
#3
startA3 = time.time()
print(Height(root3))
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(A3)
#4
startA4 = time.time()
print(Height(root4))
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(A4)
#5
startA5 = time.time()
print(Height(root5))
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(A5)
#6
startA6 = time.time()
print(Height(root6))
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(A6)
#7
startA7 = time.time()
print(Height(root7))
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(A7)
#8
startA8 = time.time()
print(Height(root8))
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(A8)
#9
startA9 = time.time()
print(Height(root9))
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(A9)



pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
pylab.title('Binary Tree Traversals')
pylab.xlabel('Input size')
pylab.ylabel('Execution time')
pylab.show()

