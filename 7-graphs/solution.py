# Given an  undirected graph G, determine if the graph is cyclic or acyclic.
# The graph is given as a list of lists where there is an edge between node i
# and node j if the list in index i contains the number j.  The graph contains
# nodes labeled 0,..., len(graph) - 1.

'''
Zain Bhaila
04/06/2020

First thing to do is create a directed graph using our undirected graph. This
makes an algorithm for cycle detection much easier if you create the directed graph
by starting at a specific node and from that node changing the undirected edges
to be directed away. If the graph is disconnected, it will have a different starting
node for that graph. Now we can determine cycles using the in degree of each vertice.
A starting vertice will have an in degree of 0. If all other vertices are 1, then
there is no cycle. If a vertice has an in degree of 2, then we have a cycle. This is true
because in order for there to be an in degree of 2, a node must be able to be reached
from multiple paths beginning at the starting node for a connected subcomponent 
of a graph. If there are multiple paths to a node in a directed graph, then there is 
cycle in the corresponding undirected graph.

Time Complexity: O(V+E) - needs to iterate over every vertice and edge to create directed graph and in degrees
Space Ceomplexity: O(V+E) - needs to create a new graph of directed edges, max size the same as original graph
'''

def has_cycle(graph):
    graph = graph.copy()
    ins = [0 for i in range(len(graph))]
    for i in range(len(graph)):
        for j in graph[i]:
            graph[j].remove(i)
    for i in range(len(graph)): 
        for j in graph[i]: 
            ins[j]+=1
            if ins[j] > 1:
                return True
    return False