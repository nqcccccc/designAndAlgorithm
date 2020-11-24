from binarytree import tree, bst, heap, Node
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

my_tree = tree(height=2, is_perfect=False)
print(my_tree)
print(len(my_tree))
# print(Height(my_tree))