# Lecture Notes #17 of CS 4349 UTDallas
from collections import defaultdict
import sys

class Graph:
     def __init__(self, vertices):

         self.vertices = vertices
         self.graph = defaultdict(list)

     def shortestPath(self, s):

         visited = [False]*self.vertices
         stack =[]
         for i in range(self.vertices):
             if visited[i] == False:
                 self.topologicalSort(s,visited,stack)
         distances = [float("Inf")] * (self.vertices)
         distances[s] = 0
         while stack:
                 i = stack.pop()
                 for node,weight in self.graph[i]:
                     if distances[node] > distances[i] + weight:
                         distances[node] = distances[i] + weight
         sys.stdout.write("{:.3f}\n".format(round(distances[-1], 3)))

     def addEdge(self,u,v,w):
         self.graph[u].append((v,w))

     def topologicalSort(self,v,visited,stack):

             visited[v] = True
             if v in self.graph.keys():
                 for node,weight in self.graph[v]:
                     if visited[node] == False:
                         self.topologicalSort(node,visited,stack)
             stack.append(v)

