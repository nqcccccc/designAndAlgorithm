# Implements sequential search with a search key as a sentinel
# Input: An array A of n elements and a search key K
# Output: The index of the first element in A[0..n − 1] whose value is equal to K or −1 if no such element is found
import time
import pylab
import random

def SequentialSearch(A,k):
    i= 0
    A.append(k)
    n = len(A)-1
    while A[i] != k:
        i+=1
    if i<n:
      return i
    else:
      return -1


#Generate random array
#Test in worst case only
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
SequentialSearch(A0,100)
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(A0)
#1
startA1 = time.time()
SequentialSearch(A1,100)
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(A1)
#2
startA2 = time.time()
SequentialSearch(A2,100)
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(A2)
#3
startA3 = time.time()
SequentialSearch(A3,100)
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(A3)
#4
startA4 = time.time()
SequentialSearch(A4,100)
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(A4)
#5
startA5 = time.time()
SequentialSearch(A5,100)
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(A5)
#6
startA6 = time.time()
SequentialSearch(A6,100)
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(A6)
#7
startA7 = time.time()
SequentialSearch(A7,100)
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(A7)
#8
startA8 = time.time()
SequentialSearch(A8,100)
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(A8)
#9
startA9 = time.time()
SequentialSearch(A9,100)
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(A9)



pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
pylab.title('Sequential Search')
pylab.xlabel('Input size')
pylab.ylabel('Execution time')
pylab.show()