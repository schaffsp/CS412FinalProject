"""
    name:  Gavin Eubank
"""


# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts

from cProfile import label


def main():
    n = 2
    actions = 0
    g = {}
    
    for edge in range(n):
        g[edge] = 1 #assume min edges
        actions += 1
    actions = complement(g, actions)
    actions = iset(g, actions)
    print("Minimum actions:", actions)

def complement(g, actions):
    for v in g:
        actions += 1
    for v in g:
        for edge in range(g[v]):
            actions += 1
        
    
    return actions

def iset(g, actions):
    labeled = 0
    while labeled < len(g):
        last = None
        for v in g:
            actions += 1
            last = v
            if v > labeled:
                for edge in range(g[v]):
                    actions += 1
        labeled += 1
        # foor loop through edges
        for edge in range(g[v]):
            actions += 1
    return actions

if __name__ == "__main__":
    main()