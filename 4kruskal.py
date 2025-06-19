def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]

def Kruskal(graph):
    edges = sorted([(w, u, v) for u in graph for v, w in graph[u]])
    parent = {v:v for v in graph}
    mst = []

    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            parent[find(parent, u)] = find(parent, v)
            mst.append((u, v, w))

    print(mst)

    return mst

graph = {
    'A' : [('B', 1), ('C', 4)],
    'B' : [('A', 1), ('C', 2), ('D', 5)],
    'C' : [('A', 4), ('B', 2), ('D', 1)],
    'D' : [('B', 5), ('C', 1)]
}

tot_cost = 0
span_tree = Kruskal(graph)

for source, target, cost in span_tree:
    tot_cost += cost  
    print("MST:", Kruskal(graph))
    print("The cost of MST is :",tot_cost)

    

