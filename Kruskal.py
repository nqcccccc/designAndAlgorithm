import pylab
import time
import random
import numpy as np

def find(i, V): 
    parent = [i for i in range(V)]
    while parent[i] != i: 
        i = parent[i] 
    return i 
  
# Does union of i and j. It returns 
# false if i and j are already in same  
# set.  
def union(i, j, V): 
    parent = [i for i in range(V)]
    a = find(i, V) 
    b = find(j,V) 
    parent[a] = b 
  
# Finds MST using Kruskal's algorithm  
def Kruskal(cost): 
    mincost = 0 # Cost of min MST 
    V = len(cost)
    parent = [i for i in range(V)]
    # Initialize sets of disjoint sets 
    for i in range(V): 
        parent[i] = i 
  
    # Include minimum weight edges one by one  
    edge_count = 0
    while edge_count < V - 1: 
        min = 9999999999999 
        a = -1
        b = -1
        for i in range(V): 
            for j in range(V): 
                if find(i,V) != find(j,V) and cost[i][j] < min: 
                    min = cost[i][j] 
                    a = i 
                    b = j 
        union(a, b, V) 
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min)) 
        edge_count += 1
        mincost += min
  
    print("Minimum cost= {}".format(mincost)) 

G0 = np.random.randint(1,100,(5,5))
G1 = np.random.randint(1,100,(10,10))
G2 = np.random.randint(1,100,(15,15))
G3 = np.random.randint(1,100,(20,20))
G4 = np.random.randint(1,100,(25,25))
G5 = np.random.randint(1,100,(30,30))
G6 = np.random.randint(1,100,(35,35))
G7 = np.random.randint(1,100,(40,40))
G8 = np.random.randint(1,100,(45,45))
G9 = np.random.randint(1,100,(50,50))

startA0 = time.time()
Kruskal(G0)
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(G0)
#1
startA1 = time.time()
Kruskal(G1)
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(G1)
#2
startA2 = time.time()
Kruskal(G2)
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(G2)
#3
startA3 = time.time()
Kruskal(G3)
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(G3)
#4
startA4 = time.time()
Kruskal(G4)
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(G4)
#5
startA5 = time.time()
Kruskal(G5)
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(G5)
#6
startA6 = time.time()
Kruskal(G6)
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(G6)
#7
startA7 = time.time()
Kruskal(G7)
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(G7)
#8
startA8 = time.time()
Kruskal(G8)
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(G8)
#9
startA9 = time.time()
Kruskal(G9)
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(G9)



pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
pylab.title("Kruskal's Algorithim")
pylab.xlabel('Input size')
pylab.ylabel('Execution time')
pylab.show()