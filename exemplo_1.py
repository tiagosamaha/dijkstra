# coding: utf-8
from dijkstra import Graph

# caminho: 1 - 2 - 3 - 6 - 5
example = { 
    1: { 2: 7, 3: 9, 6: 14},
    2: { 1: 7, 3: 10, 4: 15 },
    3: { 1: 9, 2: 10, 4: 11, 6: 2 },
    4: { 2: 15, 3: 11, 5: 6 },
    5: { 4: 6, 6: 9 },
    6: { 1: 14, 3: 2, 5: 9 },
}

graph = Graph(example, 1, 5)
graph.dijkstra()

print "Melhor caminho: " + str(graph.shortest_path())
print "Distâncias por vértice: " + str(graph.shortest_path_distance())
