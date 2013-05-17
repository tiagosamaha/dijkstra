# coding: utf-8
from dijkstra import Graph

example = { 
    'a': { 'b': 12, 'c': 4 },
    'b': { 'a': 12, 'd': 5, 'e': 3 },
    'c': { 'a': 4, 'd': 2, 'f': 6 },
    'd': { 'b': 5, 'c': 2, 'g': 8 },
    'e': { 'b': 3, 'h': 7 },
    'f': { 'c': 6, 'g': 5 },
    'g': { 'd': 8, 'f': 5, 'h': 3 },
    'h': { 'e': 7, 'g': 3 },
}

graph = Graph(example, 'a', 'h')
graph.dijkstra()

print "Melhor caminho: " + str(graph.shortest_path())
print "Distâncias por vértice: " + str(graph.shortest_path_distance())