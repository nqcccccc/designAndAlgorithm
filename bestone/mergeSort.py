import pylab
import time
import myLibrary as lib

# Sorts array A[0..n − 1] by recursive mergesort
# Input: An array A[0..n − 1] of orderable elements
# Output: Array A[0..n − 1] sorted in nondecreasing order
def MergeSort(A):
    n = len(A)
    if(n>1):
        B = A[:n//2].copy()
        C = A[n//2:].copy()
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
    p = len(B)
    q = len(C)
    while i < p and j < q:
        if B[i] <= C[j]:
            A[k]=B[i]
            i=i+1
        else:
            A[k]=C[j]
            j=j+1
        k=k+1
    if i == p:
        A[k:p+q]=C[j:q].copy()
    else:
        A[k:p+q]=B[i:p].copy()

# A = [8, 3, 2, 9, 7, 1, 5, 4]
# MergeSort(A)
# print(A)
# [1, 2, 3, 4, 5, 7, 8, 9]

#Plot
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
pylab.ylabel('Execution time (Seconds)')
pylab.show()
