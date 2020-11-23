from collections import defaultdict 
import pylab
import time
import random
import numpy as np
  
class Graph: 
  
    def minDistance(self,dist,queue): 
        # Initialize min value and min_index as -1 
        minimum = float("Inf") 
        min_index = -1
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 
  
    # def printPath(self, parent, j): 
    #     if parent[j] == -1 :  
    #         print(j,)
    #         return
    #     self.printPath(parent , parent[j]) 
    #     print(j,)
          
    # def printSolution(self, dist, parent): 
    #     s = 0
    #     print("Vertex \t\tDistance from Source\tPath") 
    #     for i in range(1, len(dist)): 
    #         print("\n%d --> %d \t\t%d \t\t\t\t\t" % (s, i, dist[i])), 
    #         self.printPath(parent,i) 
  
  
# Dijkstra’s algorithm for single-source shortest paths
# Input: A weighted connected graph G = V, E with nonnegative weights
# and its vertex s
# Output: The length dv of a shortest path from s to v
# and its penultimate vertex pv for every vertex v in V
    def Dijkstra(self, G, s): 
  
        row = len(G) 
        col = len(G[0]) 
        dist = [float("Inf")] * row 
        parent = [-1] * row 
        dist[s] = 0
        queue = [] 
        for i in range(row): 
            queue.append(i) 
        while queue: 
            u = self.minDistance(dist,queue)  
            queue.remove(u) 
            for i in range(col): 
                if G[u][i] and i in queue: 
                    if dist[u] + G[u][i] < dist[i]: 
                        dist[i] = dist[u] + G[u][i] 
                        parent[i] = u 
        # self.printSolution(dist,parent) 
  
g0= Graph() 
g1= Graph() 
g2= Graph() 
g3= Graph() 
g4= Graph() 
g5= Graph() 
g6= Graph() 
g7= Graph() 
g8= Graph() 
g9= Graph() 
  
G0 = np.random.randint(0,100,(5,5))
G1 = np.random.randint(0,100,(10,10))
G2 = np.random.randint(0,100,(15,15))
G3 = np.random.randint(0,100,(20,20))
G4 = np.random.randint(0,100,(25,25))
G5 = np.random.randint(0,100,(30,30))
G6 = np.random.randint(0,100,(35,35))
G7 = np.random.randint(0,100,(40,40))
G8 = np.random.randint(0,100,(45,45))
G9 = np.random.randint(0,100,(50,50))


startA0 = time.time()
g0.Dijkstra(G0,0) 
stopA0 = time.time()
timeA0 = stopA0 - startA0
sizeA0 = len(G0)
#1
startA1 = time.time()
g1.Dijkstra(G1,0)
stopA1 = time.time()
timeA1 = stopA1 - startA1
sizeA1 = len(G1)
#2
startA2 = time.time()
g2.Dijkstra(G2,0)
stopA2 = time.time()
timeA2 = stopA2 - startA2
sizeA2 = len(G2)
#3
startA3 = time.time()
g3.Dijkstra(G3,0)
stopA3 = time.time()
timeA3 = stopA3 - startA3
sizeA3 = len(G3)
#4
startA4 = time.time()
g4.Dijkstra(G4,0)
stopA4 = time.time()
timeA4 = stopA4 - startA4
sizeA4 = len(G4)
#5
startA5 = time.time()
g5.Dijkstra(G5,0)
stopA5 = time.time()
timeA5 = stopA5 - startA5
sizeA5 = len(G5)
#6
startA6 = time.time()
g6.Dijkstra(G6,0)
stopA6 = time.time()
timeA6 = stopA6 - startA6
sizeA6 = len(G6)
#7
startA7 = time.time()
g7.Dijkstra(G7,0)
stopA7 = time.time()
timeA7 = stopA7 - startA7
sizeA7 = len(G7)
#8
startA8 = time.time()
g8.Dijkstra(G8,0)
stopA8 = time.time()
timeA8 = stopA8 - startA8
sizeA8 = len(G8)
#9
startA9 = time.time()
g9.Dijkstra(G9,0)
stopA9 = time.time()
timeA9 = stopA9 - startA9
sizeA9 = len(G9)



pylab.plot([sizeA0,sizeA1,sizeA2,sizeA3,sizeA4,sizeA5,sizeA6,sizeA7,sizeA8,sizeA9],[timeA0,timeA1,timeA2,timeA3,timeA4,timeA5,timeA6,timeA7,timeA8,timeA9],'ro-')
pylab.title("Dijkstra's Algorithim")
pylab.xlabel('Input size')
pylab.ylabel('Execution time')
pylab.show()  
  
