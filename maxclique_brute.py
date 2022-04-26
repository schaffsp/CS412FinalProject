#Ben Girardi
# Brute force clique solution

from itertools import combinations

def main():
    g = {}


    # check for complete graph
    def check_clique(nodes):
        nonlocal g
        for i in range(0, len(nodes) - 1):
            for j in range(i + 1, len(nodes)):
                if nodes[j] not in g[nodes[i]]:
                    return False, None

        return True, nodes
                  

    num = int(input())

    # create adj list
    for i in range(0,num):
        line = list(input().strip().split())
        vertex = line[0]
        edges = line[1:]

        if vertex not in g:
            g[vertex] = []
        for e in edges:
            if e not in g:
                g[e] = []

        g[vertex] = edges

   
    # change? 
    max_clique = 2

    for i in range(2, num + 1):

        # create combinations from 2 to #V
        combs = list(combinations(g.keys(), i))

        for vertices in combs:
            isClique, clique = check_clique(vertices)

            if isClique:
                clique_size = len(clique)
                max_clique = max(max_clique, clique_size)
            
    print("max clique", max_clique)

if __name__ == "__main__":
    main()