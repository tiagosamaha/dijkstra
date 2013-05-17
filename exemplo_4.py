# coding: utf-8
from dijkstra import Graph

example = { 
    1: { 2: 1, 6: 10 },
    2: { 1: 1, 3: 2, 5: 5, 6: 8 },
    3: { 2: 2, 4: 1, 5: 5, 6: 6 },
    4: { 3: 1, 5: 1 },
    5: { 2: 5, 4: 1, 3: 5, 6: 3 },
    6: { 1: 10, 3: 6, 5: 3, 2: 8 },
}

graph = Graph(example, 1, 6)
graph.dijkstra()

print "Melhor caminho: " + str(graph.shortest_path())
print "Distâncias por vértice: " + str(graph.shortest_path_distance())
