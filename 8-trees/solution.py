from typing import Generator, Tuple


# Given a graph (undirected), determine whether or not it is a tree.
# The input will be fairly abstract as to leave the graph implementation up to the student.
# The input will have the number of nodes and then a generator* of edges.
# Nodes are numbered 0 to n-1 (inclusive).

# *you can iterate over the elements of a generator (as shown in the starter code)

# It is guaranteed that the number of vertices N <= 1e6 aka 1 million.
# The edge generator will not contain any duplicates.

# Recall that a tree is a connected acyclic graph.
# There are many equivalent definitions that will lead to different implementations.

def is_tree(n: int, edges: Generator[Tuple[int, int], None, None]) -> bool:
    for u, v in edges:
        pass
