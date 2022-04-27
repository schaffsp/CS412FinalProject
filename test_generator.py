"""
    name:  Sam Schafft, Gavin Eubank
"""
import random

def main():
    # define a test with n number of verticies, with a clique size m
    # m MUST BE LESS THAN n
    print("Input number of verticies: ")
    n = int(input())
    print("Input clique size: ")
    m = int(input())
    clique = range(m)
    

    # Random Generation code:
    """
        n = random.randrange(3, 50) # change 50 for max nodes
        clique = set(random.sample([i for i in range(n)], k = random.randrange(2, n)))
    """

    adjacency_list = [[] for _ in range(n)]
    print("TEST CASE IS: ")
    print(n)

    for v in clique:
        for u in clique:
            if v != u:
                adjacency_list[v].append(u)
    # ADD RANDOM STUFF TO THE LIST
    for i in range(len(adjacency_list)):
        if i not in clique:
            for i in range(random.randrange(0, len(clique) - 1)):
                nV = random.randrange(0, n)
                if nV not in adjacency_list[i]:
                    adjacency_list[i].append(nV)

    for i in range(len(adjacency_list)):
        print(i, " ".join(str(num) for num in adjacency_list[i]))

    print('\nMax Clique: ', len(clique))


if __name__ == "__main__":
    main()