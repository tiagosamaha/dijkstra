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
        vertex = G[V].copy()
        for neighbor in G[V]:
            if S[neighbor]:
                vertex.pop(neighbor)
        
        if not vertex == {}:
            for v, d in vertex.iteritems():
                D[v] = D[V] + d
            distance, vertex = min([ (d,v) for v, d in vertex.iteritems() ])
            P[vertex] = V
        else:
            break
        
        S[V] = True
        V = vertex

    print "Prcedentes: " + str(P)
    print "Distâncias: " + str(D)

print "Exemplo 1"
dijkstra(ex1, 1, 5)
print 
print "Exemplo 2"
dijkstra(ex2, 1, 6)