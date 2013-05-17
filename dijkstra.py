# coding: utf-8
#!/bin/python


class Graph:

    def __init__(self, G, start, end):
        self.G = G
        self.start = start
        self.end = end
        self.D = {} # distancia
        self.P = {} # precendetes
        self.S = {}
    
        for i in self.G:
            self.D[i] = float("inf")
            self.P[i] = -1
            self.S[i] = False
        
        self.D[self.start] =  0
        self.P[self.start] = -1
    
        self.V = self.start
        
    def dijkstra(self):
        while True:
            neighbors_of_vertex = self.G[self.V].copy()
            for neighbor in self.G[self.V]:
                if self.S[neighbor]:
                    neighbors_of_vertex.pop(neighbor)
        
            if not neighbors_of_vertex == {}:
                for v, d in neighbors_of_vertex.iteritems():
                    if self.D[self.V] + d < self.D[v]:
                        self.D[v] = self.D[self.V] + d
                distance, vertex = min([ (d,v) for v, d in neighbors_of_vertex.iteritems() ])
                self.P[vertex] = self.V
            else:
                break
        
            self.S[self.V] = True
            self.V = vertex
    
        return self.P, self.D

    def shortest_path(self):
        distance = 0
        path = [self.end]
        back = self.end
        while back != self.start:
            back = self.P[back]
            path.append(back)
        path.reverse()
        return path
    
    def shortest_path_distance(self):
        total = 0
        distances = []
        for vertex in self.shortest_path():
            total = self.D[vertex] + total
            distances.append(self.D[vertex])
        return total, distances
        