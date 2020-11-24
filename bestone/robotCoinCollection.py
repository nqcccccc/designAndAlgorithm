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

# A0= [[53, 18, 26, 96, 63],
#  [63, 24, 42,  2, 82],
#  [54, 99, 60, 57, 58],
#  [86, 37, 52, 55, 31],
#  [75, 74, 11, 50,  2]]
# print(A0)
# print(RobotCoinCollection(A0))
# #493
A0= np.random.randint(1,100,(5,5))
A1 = np.random.randint(1,100,(10,10))
A2 = np.random.randint(1,100,(15,15))
A3 = np.random.randint(1,100,(20,20))
A4 = np.random.randint(1,100,(25,25))
A5 = np.random.randint(1,100,(30,30))
A6 = np.random.randint(1,100,(35,35))
A7 = np.random.randint(1,100,(40,40))
A8 = np.random.randint(1,100,(45,45))
A9 = np.random.randint(1,100,(50,50))

#0
startA0 = time.time()
RobotCoinCollection(A0)
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(A0)*len(A0[0])
#1
startA1 = time.time()
RobotCoinCollection(A1)
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(A1)*len(A1[0])
#2
startA2 = time.time()
RobotCoinCollection(A2)
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(A2)*len(A2[0])
#3
startA3 = time.time()
RobotCoinCollection(A3)
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(A3)*len(A3[0])
#4
startA4 = time.time()
RobotCoinCollection(A4)
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(A4)*len(A4[0])
#5
startA5 = time.time()
RobotCoinCollection(A5)
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(A5)*len(A5[0])
#6
startA6 = time.time()
RobotCoinCollection(A6)
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(A6)*len(A6[0])
#7
startA7 = time.time()
RobotCoinCollection(A7)
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(A7)*len(A7[0])
#8
startA8 = time.time()
RobotCoinCollection(A8)
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(A8)*len(A8[0])
#9
startA9 = time.time()
RobotCoinCollection(A9)
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(A9)*len(A9[0])


# vẽ 3d
pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
pylab.title('Robot Coin Collection')
pylab.xlabel('Input size')
pylab.ylabel('Execution time (Seconds)')
pylab.show()
