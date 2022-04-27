"""
    name:  Sam Schafft
"""
import itertools
import random

def main():
    # define a test with n number of verticies
    n = 10
    print(n)

    adjacency_list = [[] for _ in range(n)]
    clique = set(random.sample([i for i in range(n)], k = random.randrange(2, n)))
    for v in clique:
        for u in clique:
            if v != u:
                adjacency_list[v].append(u)
    for i in range(len(adjacency_list)):
        if i not in clique:
            for i in range(random.randrange(0, len(clique) - 1)):
                adjacency_list[i].append(random.randrange(0, n))

    for i in range(len(adjacency_list)):
        print(i, " ".join(str(num) for num in adjacency_list[i]))

    print('\nMax Clique: ', len(clique))


if __name__ == "__main__":
    main()