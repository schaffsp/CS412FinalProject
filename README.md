The max clique decision problem is given an undirected graph G, and an integer k, is there a clique within G of size k.

The optimization problem is finding the maximum sized clique within a graph G.

Input for the problem: undirected, unwieghted graph formatted as an adjacency list in the same way as previous labs preceded by an integer n repesenting the number of verticies / length of adjacency list.

example input: [Max clique in the example is 0, 1, 2]
5
0 1 2
1 0 2
2 0 1 3
3 2 4
4 3

**Note: the upperbound would be the maximum degree in the graph since it is impossible to have a clique larger than the largest degree.
