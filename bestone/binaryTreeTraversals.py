import pylab
import time
import myLibrary as lib

# Computes recursively the height of a binary tree
# Input: A binary tree T
# Output: The height of T
def Height(T):
	if T is None:
		return -1
	return max(Height(T.left), Height(T.right))+1

# A = [22, 20, 88, 84, 65, 10, 4, 75, 68, 6]
# print(Height(A))
# #3

root0 = lib.tree(height=0, is_perfect=False)
root1 = lib.tree(height=1, is_perfect=False)
root2 = lib.tree(height=2, is_perfect=False)
root3 = lib.tree(height=3, is_perfect=False)
root4 = lib.tree(height=4, is_perfect=False)
root5 = lib.tree(height=5, is_perfect=False)
root6 = lib.tree(height=6, is_perfect=False)
root7 = lib.tree(height=7, is_perfect=False)
root8 = lib.tree(height=8, is_perfect=False)
root9 = lib.tree(height=9, is_perfect=False)

#0
startA0 = time.time()
print(Height(root0))
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(root0)
#1
startA1 = time.time()
print(Height(root1))
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(root1)
#2
startA2 = time.time()
print(Height(root2))
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(root2)
#3
startA3 = time.time()
print(Height(root3))
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(root3)
#4
startA4 = time.time()
print(Height(root4))
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(root4)
#5
startA5 = time.time()
print(Height(root5))
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(root5)
#6
startA6 = time.time()
print(Height(root6))
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(root6)
#7
startA7 = time.time()
print(Height(root7))
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(root7)
#8
startA8 = time.time()
print(Height(root8))
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(root8)
#9
startA9 = time.time()
print(Height(root9))
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(root9)

pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
pylab.title('Binary Tree Traversals')
pylab.xlabel('Input size')
pylab.ylabel('Execution time (Seconds)')
pylab.show()

