"""
    name:  Chris Cleveland
    
"""
import sys
def main():
    n = int(input())
    edges = [(input().split()) for _ in range(int(n))]
    graph = {}
    maxEdges = 0
    for edge in edges:
        graph[edge[0]] = edge[1:]
        if len(edge) > maxEdges:
            maxEdges = len(edge)
    compGraph = complement(graph)
    ans = independentSet(compGraph)
    count = 0
    for node in ans:
        print("node is", ans[node])
        if ans[node] == 1:  
            count+=1
    print(ans)
    print("max clique is ", count)

"""
    Creats a graphs complement
"""
def complement(graph):
    verts = graph.keys()
    comp = {}
    for vert in verts:
        comp[vert] = []
    for vert in graph:
        for v in verts:
            if v not in graph[vert] and vert is not v:
                comp[vert].append(v)
    return comp

"""
    greedy method to find the independent set of a graph
    which in turn gives its max clique
"""
def independentSet(graph):
    verts = list(graph.keys())
    labeled = {}
    while len(labeled) < len(verts):
        min = sys.maxsize
        count = 0
        currNode = verts[0]
        for v in verts:
            if v not in labeled:
                for node in graph[v]:
                    if node not in labeled:
                        count += 1
                if count < min:
                    min = count
                    currNode = v
        labeled[currNode] = 1
        for node in graph[currNode]:
            labeled[node] = 0
    return labeled

if __name__ == "__main__":
    main()