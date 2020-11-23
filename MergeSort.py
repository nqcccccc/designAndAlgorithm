import pylab
import time
import random

# Sorts array A[0..n − 1] by recursive mergesort
# Input: An array A[0..n − 1] of orderable elements
# Output: Array A[0..n − 1] sorted in nondecreasing order
def MergeSort(A):
    if(len(A)>1):
        mid = len(A)//2
        B = A[:mid]
        C = A[mid:]
        MergeSort(B)
        MergeSort(C)
        Merge(B,C,A)

# Merges two sorted arrays into one sorted array
# Input: Arrays B[0..p − 1] and C[0..q − 1] both sorted
# Output: Sorted array A[0..p + q − 1] of the elements of B and C
def Merge(B,C,A):
    i=0
    j=0
    k=0
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            A[k]=B[i]
            i=i+1
        else:
            A[k]=C[j]
            j=j+1
        k=k+1
    
    while i < len(B):
        A[k]=B[i]
        i=i+1
        k=k+1

    while j < len(C):
        A[k]=C[j]
        j=j+1
        k=k+1

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
MergeSort(A0)
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(A0)
#1
startA1 = time.time()
MergeSort(A1)
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(A1)
#2
startA2 = time.time()
MergeSort(A2)
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(A2)
#3
startA3 = time.time()
MergeSort(A3)
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(A3)
#4
startA4 = time.time()
MergeSort(A4)
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(A4)
#5
startA5 = time.time()
MergeSort(A5)
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(A5)
#6
startA6 = time.time()
MergeSort(A6)
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(A6)
#7
startA7 = time.time()
MergeSort(A7)
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(A7)
#8
startA8 = time.time()
MergeSort(A8)
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(A8)
#9
startA9 = time.time()
MergeSort(A9)
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(A9)



pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
pylab.title('Merge Sort')
pylab.xlabel('Input size')
pylab.ylabel('Execution time')
pylab.show()