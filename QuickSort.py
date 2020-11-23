import pylab
import time
import random

# Sorts a subarray by quicksort
# Input: Subarray of array A[0..n − 1], defined by its left and right 
# indices l and r
# Output: Subarray A[l..r] sorted in nondecreasing order

def QuickSort(A,l,r):
    if l < r:
        s = Partition(A,l,r)
        QuickSort(A,l,s-1)
        QuickSort(A,s+1,r)

# Partitions a, using the last element as a pivot
# Input: Subarray of array A[0..n − 1], defined by its left and right
# indices l and r (l < r)
# Output: Partition of A[l..r], with the split position returned as
# this function’s value

def Partition(A,l,r):
    i = (l-1)
    p = A[r]     
    for j in range(l, r):
        if A[j] <= p:
            i = i+1
            A[i], A[j] = A[j], A[i]
 
    A[i+1], A[r] = A[r], A[i+1]
    return (i+1)

def ranGen(n):
    randomlist = []
    for i in range(0,n):
        key = random.randint(1,99)
        randomlist.append(key)
    return randomlist


A0 = ranGen(10)
A1 = ranGen(100)
A2 = ranGen(200)
A3 = ranGen(300)
A4 = ranGen(400)
A5 = ranGen(500)
A6 = ranGen(600)
A7 = ranGen(700)
A8 = ranGen(800)
A9 = ranGen(900)

#0
startA0 = time.time()
QuickSort(A0,0,len(A0)-1)
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(A0)
#1
startA1 = time.time()
QuickSort(A1,0,len(A1)-1)
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(A1)
#2
startA2 = time.time()
QuickSort(A2,0,len(A2)-1)
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(A2)
#3
startA3 = time.time()
QuickSort(A3,0,len(A3)-1)
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(A3)
#4
startA4 = time.time()
QuickSort(A4,0,len(A4)-1)
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(A4)
#5
startA5 = time.time()
QuickSort(A5,0,len(A5)-1)
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(A5)
#6
startA6 = time.time()
QuickSort(A6,0,len(A6)-1)
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(A6)
#7
startA7 = time.time()
QuickSort(A7,0,len(A7)-1)
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(A7)
#8
startA8 = time.time()
QuickSort(A8,0,len(A8)-1)
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(A8)
#9
startA9 = time.time()
QuickSort(A9,0,len(A9)-1)
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(A9)



pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
pylab.title('Quick Sort')
pylab.xlabel('Input size')
pylab.ylabel('Execution time')
pylab.show()
