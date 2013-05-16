# coding: utf-8
#!/bin/python

# caminho: 1 - 2 - 3 - 6 - 5
ex1 = { 
    1: { 2: 7, 3: 9, 6: 14},
    2: { 1: 7, 3: 10, 4: 15 },
    3: { 1: 9, 2: 10, 4: 11, 6: 2 },
    4: { 2: 15, 3: 11, 5: 6 },
    5: { 4: 6, 6: 9 },
    6: { 1: 14, 3: 2, 5: 9 },
}

# caminho: 1 - 2 - 4 - 5 - 3 - 6
ex2 = { 
    1: { 2: 1, 4: 3 },
    2: { 1: 1, 4: 1, 3: 5 },
    3: { 2: 5, 5: 3, 6: 3 },
    4: { 1: 3, 2: 1, 5: 1 },
    5: { 4: 1, 3: 3, 6: 7 },
    6: { 3: 3, 5: 7 },
}

def dijkstra(G, start, end):
    D = {} # distancia
    P = {} # precendetes
    S = {}
    
    for i in G:
        D[i] = float("inf")
        P[i] = -1
        S[i] = False
    
    D[start] =  0
    P[start] = -1
    
    V = start

    while True:
        neighbors_of_vertex = G[V].copy()
        for neighbor in G[V]:
            if S[neighbor]:
                neighbors_of_vertex.pop(neighbor)
        
        if not neighbors_of_vertex == {}:
            for v, d in neighbors_of_vertex.iteritems():
                if D[V] + d < D[v]:
                    D[v] = D[V] + d
            distance, vertex = min([ (d,v) for v, d in neighbors_of_vertex.iteritems() ])
            P[vertex] = V
        else:
            break
        
        S[V] = True
        V = vertex
    
    return P, D

def shortest_path(start, end, previous):
    path = [end]
    back = end
    while back != start:
        back = previous[back]
        path.append(back)
    path.reverse()
    print path

print "Exemplo 1"
precedentes, distancias = dijkstra(ex1, 1, 5)
shortest_path(1, 5, precedentes)
print distancias
print 
print "Exemplo 2"
precedentes, distancias = dijkstra(ex2, 1, 6)
shortest_path(1, 6, precedentes)
print distancias