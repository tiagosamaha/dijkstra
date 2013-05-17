# coding: utf-8
from dijkstra import Graph

# caminho: 1 - 2 - 4 - 5 - 3 - 6
example = { 
    1: { 2: 1, 4: 3 },
    2: { 1: 1, 4: 1, 3: 5 },
    3: { 2: 5, 5: 3, 6: 3 },
    4: { 1: 3, 2: 1, 5: 1 },
    5: { 4: 1, 3: 3, 6: 7 },
    6: { 3: 3, 5: 7 },
}

graph = Graph(example, 1, 6)
graph.dijkstra()

print "Melhor caminho: " + str(graph.shortest_path())
print "Distâncias por vértice: " + str(graph.shortest_path_distance())