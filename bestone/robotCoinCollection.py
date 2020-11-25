import time
import pylab
import random
import numpy as np

# Applies dynamic programming to compute the largest number of
# coins a robot can collect on an n × m board by starting at (1, 1)
# and moving right and down from upper left to down right corner
# Input: Matrix C[1..n, 1..m] whose elements are equal to 1 and 0
# for cells with and without a coin, respectively
# Output: Largest number of coins the robot can bring to cell (n, m)
def RobotCoinCollection(C):
    n = len(C)# rows
    m = len(C[0]) # col
    F = [[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        F[i][1] = F[i-1][1]+C[i-1][0]
        for j in range(1,m+1):
            F[i][j]=max(F[i-1][j],F[i][j-1])+C[i-1][j-1]
    return F[n][m]

A= [[1, 1, 0, 0, 1, 0, 1, 0, 0, 0],
 [1, 0, 1, 1, 0, 0, 1, 0, 0, 1], 
 [1, 0, 1, 0, 0, 0, 1, 0, 0, 1], 
 [1, 1, 0, 0, 0, 1, 0, 1, 0, 1], 
 [0, 1, 0, 0, 0, 0, 0, 1, 0, 1]]
print(A)
print(RobotCoinCollection(A))
#9
A0= np.random.randint(0,2,(5,10))
A1 = np.random.randint(0,2,(100,150))
A2 = np.random.randint(0,2,(200,250))
A3 = np.random.randint(0,2,(300,350))
A4 = np.random.randint(0,2,(400,450))
A5 = np.random.randint(0,2,(500,550))
A6 = np.random.randint(0,2,(600,650))
A7 = np.random.randint(0,2,(700,750))
A8 = np.random.randint(0,2,(800,850))
A9 = np.random.randint(0,2,(900,950))

#0
startA0 = time.time()
RobotCoinCollection(A0)
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(A0)
sizeA01 = len(A0[0])
#1
startA1 = time.time()
RobotCoinCollection(A1)
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(A1)
sizeA11 = len(A1[0])
#2
startA2 = time.time()
RobotCoinCollection(A2)
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(A2)
sizeA21 = len(A2[0])
#3
startA3 = time.time()
RobotCoinCollection(A3)
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(A3)
sizeA31 = len(A3[0])
#4
startA4 = time.time()
RobotCoinCollection(A4)
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(A4)
sizeA41 = len(A4[0])
#5
startA5 = time.time()
RobotCoinCollection(A5)
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(A5)
sizeA51 = len(A5[0])
#6
startA6 = time.time()
RobotCoinCollection(A6)
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(A6)
sizeA61 = len(A6[0])
#7
startA7 = time.time()
RobotCoinCollection(A7)
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(A7)
sizeA71 = len(A7[0])
#8
startA8 = time.time()
RobotCoinCollection(A8)
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(A8)
sizeA81 = len(A8[0])
#9
startA9 = time.time()
RobotCoinCollection(A9)
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(A9)
sizeA91 = len(A9[0])


# vẽ 3d
pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'o-',label = "Rows")
pylab.plot([sizeA01,sizeA11,sizeA21,sizeA31,sizeA41,sizeA51,sizeA61,sizeA71,sizeA81,sizeA91],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'*-',label = "Cols")
pylab.title('Robot Coin Collection')
pylab.xlabel('Input size')
pylab.ylabel('Execution time (Seconds)')
pylab.legend()
pylab.show()
