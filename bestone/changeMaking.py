import time
import pylab
import myLibrary as lib

# Applies dynamic programming to find the minimum number of coins
# of denominations d1 < d2 < . . . < dm where d1 = 1 that add up to a
# given amount n
# Input: Positive integer n and array D[1..m] of increasing positive
# integers indicating the coin denominations where D[1]= 1
# Output: The minimum number of coins that add up to n

def ChangeMaking(D,n):
    m = len(D)-1
    F = [0 for _ in range(n+1)]#+1 vì xếp từ 1-> m
    for i in range(1, n+1):
        temp = 9999
        j = 1
        while j <= m and i>= D[j]:
            temp = min(F[i-D[j]],temp)
            j = j+1
        F[i] = temp+1
    return F[n]

# A =  [1,2,4] 
# print(ChangeMaking(A,20))
# #5

A0 = lib.listGen(10)
A1 = lib.listGen(100)
A2 = lib.listGen(200)
A3 = lib.listGen(300)
A4 = lib.listGen(400)
A5 = lib.listGen(500)
A6 = lib.listGen(600)
A7 = lib.listGen(700)
A8 = lib.listGen(800)
A9 = lib.listGen(900)

#0
startA0 = time.time()
ChangeMaking(A0,A0[-1]*2)
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(A0)
#1
startA1 = time.time()
ChangeMaking(A1,A1[-1]*2)
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(A1)
#2
startA2 = time.time()
ChangeMaking(A2,A2[-1]*2)
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(A2)
#3
startA3 = time.time()
ChangeMaking(A3,A3[-1]*2)
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(A3)
#4
startA4 = time.time()
ChangeMaking(A4,A4[-1]*2)
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(A4)
#5
startA5 = time.time()
ChangeMaking(A5,A5[-1]*2)
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(A5)
#6
startA6 = time.time()
ChangeMaking(A6,A6[-1]*2)
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(A6)
#7
startA7 = time.time()
ChangeMaking(A7,A7[-1]*2)
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(A7)
#8
startA8 = time.time()
ChangeMaking(A8,A8[-1]*2)
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(A8)
#9
startA9 = time.time()
ChangeMaking(A9,A9[-1]*2)
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(A9)



pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
pylab.title('Change Making')
pylab.xlabel('Input size')
pylab.ylabel('Execution time (Seconds)')
pylab.show()