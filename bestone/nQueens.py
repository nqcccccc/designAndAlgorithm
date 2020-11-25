import sys
import random
import time
import pylab
import numpy as np

def is_attack(i, j, board, N):
  # checking for column j
  for k in range(1, i):
    if(board[k][j] == 1):
      return True

  # checking upper right diagonal
  k = i-1
  l = j+1
  while (k>=1 and l<=N):
    if (board[k][l] == 1):
      return True
    k=k+1
    l=l+1

  # checking upper left diagonal
  k = i-1
  l = j-1
  while (k>=1 and l>=1):
    if (board[k][l] == 1):
      return True
    k=k-1
    l=l-1

  return False

def n_queen(row, n, N, board):
  if (n==0):
    return True

  for j in range(1, N+1):
    if(not(is_attack(row, j, board, N))):
      board[row][j] = 1

      if (n_queen(row+1, n-1, N, board)):
        return True

      board[row][j] = 0 #backtracking
  return False

x = []
y = []
if __name__ == '__main__':
    board = [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],]

    n_queen(1, 9, 9, board)

    #printing the matix
    for i in range(1, 10):
        print(board[i][1:])
# for i in range(5,20,5):
#   board = [[0]*i for _ in range(i)]
#   N = i
#   start = time.time()
#   N_queen(i)
#   for j in board:
#     print (j)
#   end = time.time()
#   x.append(i)
#   y.append(end-start)

# for i in range(4,1000,100):
#     board = [[0]*i for _ in range(i)]
#     start = time.time()
#     N_queen(i)
#     stop = time.time()
#     timetemp = stop - start
#     time.append(timetemp)
#     size.append(i)


# pylab.plot(x,y,'ro-')
# pylab.title("N Queens Algorithim")
# pylab.xlabel('Input size')
# pylab.ylabel('Execution time (Seconds)')
# pylab.show()