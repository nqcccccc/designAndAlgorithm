import pylab
import time
import sys
import numpy as np
import networkx as nx

def Vertex(n):
  list =[]
  for i in range(n):
    list.append(i)
  return list

def find(G,VT,V):
  e = [-1, -1]
  min = 9999999
  for v in VT:
    for u in V:
      if(G[v][u] < min and G[v][u] != 0):
        min = G[v][u]
        e[0] = v
        e[1] = u
  return e
# Prim’s algorithm for constructing a minimum spanning tree
# Input: A weighted connected graph G = V, E
# Output: ET , the set of edges composing a minimum spanning tree of G
# VT ← {v0} 
# the set of tree vertices can be initialized with any vertex
# ET ← ∅

def Prim(G):
    v = np.random.randint(0,len(G))
    V = list(range(0, len(G)))
    VT = []
    VT.append(v)
    V.remove(v)
    ET = []
    for i in range(1, len(G)):
        e = find(G,VT, V)
        VT.append(e[1])
        ET.append(e)
        V.remove(e[1])
    return ET

G = [[89, 27, 21, 48, 45],
 [96,  5, 86, 11, 45],
 [ 8, 60, 17, 80,  6],
 [70, 45, 68, 17, 47],
 [17, 99, 17, 64, 49]]

print(Prim(G))
# #[[4, 0], [4, 2], [0, 1], [1, 3]]
# G0 = np.random.randint(0,100,(5,5))
# G1 = np.random.randint(0,100,(100,100))
# G2 = np.random.randint(0,100,(150,150))
# G3 = np.random.randint(0,100,(200,200))
# G4 = np.random.randint(0,100,(250,250))
# G5 = np.random.randint(0,100,(300,300))
# G6 = np.random.randint(0,100,(350,350))
# G7 = np.random.randint(0,100,(400,400))
# G8 = np.random.randint(0,100,(450,450))
# G9 = np.random.randint(0,100,(500,500))

# startA0 = time.time()
# Prim(G0)
# stopA0 = time.time()
# timeA0 = stopA0 - startA0
# sizeA0 = len(G0)
# #1
# startA1 = time.time()
# Prim(G1)
# stopA1 = time.time()
# timeA1 = stopA1 - startA1
# sizeA1 = len(G1)
# #2
# startA2 = time.time()
# Prim(G2)
# stopA2 = time.time()
# timeA2 = stopA2 - startA2
# sizeA2 = len(G2)
# #3
# startA3 = time.time()
# Prim(G3)
# stopA3 = time.time()
# timeA3 = stopA3 - startA3
# sizeA3 = len(G3)
# #4
# startA4 = time.time()
# Prim(G4)
# stopA4 = time.time()
# timeA4 = stopA4 - startA4
# sizeA4 = len(G4)
# #5
# startA5 = time.time()
# Prim(G5)
# stopA5 = time.time()
# timeA5 = stopA5 - startA5
# sizeA5 = len(G5)
# #6
# startA6 = time.time()
# Prim(G6)
# stopA6 = time.time()
# timeA6 = stopA6 - startA6
# sizeA6 = len(G6)
# #7
# startA7 = time.time()
# Prim(G7)
# stopA7 = time.time()
# timeA7 = stopA7 - startA7
# sizeA7 = len(G7)
# #8
# startA8 = time.time()
# Prim(G8)
# stopA8 = time.time()
# timeA8 = stopA8 - startA8
# sizeA8 = len(G8)
# #9
# startA9 = time.time()
# Prim(G9)
# stopA9 = time.time()
# timeA9 = stopA9 - startA9
# sizeA9 = len(G9)



# pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
# pylab.title("Prim's Algorithim")
# pylab.xlabel('Input size')
# pylab.ylabel('Execution time (Seconds)')
# pylab.show()