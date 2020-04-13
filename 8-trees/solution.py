from typing import Generator, Tuple
import collections

# Given a graph (undirected), determine whether or not it is a tree.
# The input will be fairly abstract as to leave the graph implementation up to the student.
# The input will have the number of nodes and then a generator* of edges.
# Nodes are numbered 0 to n-1 (inclusive).

# *you can iterate over the elements of a generator (as shown in the starter code)

# It is guaranteed that the number of vertices N <= 1e6 aka 1 million.
# The edge generator will not contain any duplicates.

# Recall that a tree is a connected acyclic graph.
# There are many equivalent definitions that will lead to different implementations.

'''
Zain Bhaila
HW8 - Trees
04/12/2020

A graph is a tree if two of three conditions are proved: number of edges is one less
than number of vertices, there are no simple cycles, the graph is connected. My
algorithm checks the edges and connectivity. First, base case, no vertices in a graph
is a tree. Then loop through edges and store in a hash while also counting the
number of edges. If the edge count is not n - 1, graph is not a tree. Now use
bfs to check for connectivity. Start at vertex 0 and traverse all connected vertices.
Add visited vertices to a hash and if hash length is the same as n, then all
nodes were visited.

Time Complexity: O(n) - max out number of edges at n - 1, bfs can only search over n - 1 edges
Space Complexity: O(n) - store edges as adjacency matrix, up to n - 1 edges
'''

# graph is a tree if is is connected and has n - 1 edges
def is_tree(n: int, edges: Generator[Tuple[int, int], None, None]) -> bool:
    if n == 0: # an empty graph is a tree
        return True

    graph = {}
    edge_count = 0
    for u, v in edges: # get edges out of generator and into graph dict
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
        edge_count += 1
        if edge_count > n - 1: # edge count cannot surpass n - 1
            return False

    if edge_count != n - 1: # graph is cyclic or disconnected if number of edges does not equal n - 1
        return False

    # BFS implementation
    visited = {0: True}
    queue = collections.deque([0]) # deque is faster than list for implementing a queue

    while queue: # bfs through graph to determine if connected
        cur = queue.popleft()

        for vert in graph[cur]: # for all adjacent vertices, check if not visited then add to queue
            if not visited.get(vert, False):
                queue.append(vert)
                visited[vert] = True

    return len(visited) == n # if all vertices were visited, then connected graph
