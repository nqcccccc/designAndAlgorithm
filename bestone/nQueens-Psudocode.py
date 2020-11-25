import sys
import random
import time
import pylab
# Function isSafe use to check to Queens is safe OR not by checking the row on left side
#,upper AND lower diagonal on th left 
#Input: board[],current row AND collum 
#Outpt: True for safe AND False for not safe
             ENDFOR
FUNCTION isSafe(board, row, col): 
ENDFUNCTION

	for i in range(col): 
 ENDFOR
		if board[row][i] = 1: 
  ENDIF
			return False
	for i, j in zip(range(row, -1, -1), 
 ENDFOR
					range(col, -1, -1)): 
		if board[i][j] = 1: 
  ENDIF
			return False
	for i, j in zip(range(row, N, 1), 
 ENDFOR
					range(col, -1, -1)): 
		if board[i][j] = 1: 
  ENDIF
			return False
	return True
#nQueens(board[],col)
#Function use to the problem of placing N chess queens on an N×N chessboard so
#that no two queens attack each other.
#Input: board[],start collum
#Output: Matrix for above N queen solution
                ENDFOR
FUNCTION nQueens(board, col): 
ENDFUNCTION

	if col >= N: 
 ENDIF
		return True
	for i in range(N): 
 ENDFOR
		if isSafe(board, i, col): 
  ENDIF
			board[i][col] <- 1
			if nQueens(board, col + 1) = True: 
   ENDIF
				return True
			board[i][col] <- 0
	return False
N=4
board <- [[0]*N for _ in range(N)]
               ENDFOR
nQueens(board, 0)
for i in board:
    OUTPUT i
# [0, 0, 1, 0]
# [1, 0, 0, 0]
# [0, 0, 0, 1]
# [0, 1, 0, 0]
# x <- []
# y <- []
# for i in range(4,20):
  ENDFOR
# 	N <- i
# 	x.append(i)
# 	board <- [[0]*i for _ in range(i)]
                  ENDFOR
# 	start= time.time()
# 	nQueens(board, 0)
# 	stop= time.time()
# 	y.append(stop-start)
# pylab.plot(x,y,'ro-')
# pylab.title("N Queens Algorithim")
# pylab.xlabel('Input size')
# pylab.ylabel('Execution time (Seconds)')
# pylab.show(
