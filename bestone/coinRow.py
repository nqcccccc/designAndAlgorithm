import time
import pylab
import myLibrary as lib

# Applies formula (8.3) bottom up to find the maximum amount of money
# that can be picked up from a coin row without picking two adjacent coins
# Input: Array C[1..n] of positive integers indicating the coin values
# Output: The maximum amount of money that can be picked up

def CoinRow(C):
    C.insert(0, 0)
    F = C
    F[0] = 0
    F[1] = C[1]
    for i in range(2,len(C)):
        F[i] = max(C[i]+F[i -2],F[i - 1])
    return F[len(C)-1]

A = [5, 1, 2, 10, 6, 2]
print(CoinRow(A))
#10
A0 = lib.ranGen(10)
A1 = lib.ranGen(100)
A2 = lib.ranGen(200)
A3 = lib.ranGen(300)
A4 = lib.ranGen(400)
A5 = lib.ranGen(500)
A6 = lib.ranGen(600)
A7 = lib.ranGen(700)
A8 = lib.ranGen(800)
A9 = lib.ranGen(900)

#0
startA0 = time.time()
CoinRow(A0)
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(A0)
#1
startA1 = time.time()
CoinRow(A1)
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(A1)
#2
startA2 = time.time()
CoinRow(A2)
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(A2)
#3
startA3 = time.time()
CoinRow(A3)
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(A3)
#4
startA4 = time.time()
CoinRow(A4)
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(A4)
#5
startA5 = time.time()
CoinRow(A5)
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(A5)
#6
startA6 = time.time()
CoinRow(A6)
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(A6)
#7
startA7 = time.time()
CoinRow(A7)
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(A7)
#8
startA8 = time.time()
CoinRow(A8)
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(A8)
#9
startA9 = time.time()
CoinRow(A9)
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(A9)



pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
pylab.title('Coin Row')
pylab.xlabel('Input size')
pylab.ylabel('Execution time')
pylab.show()