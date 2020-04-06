# problem 1 - Cycle graph
# store graph as a hashmap of vertices mapped to all other vertices they have an edge to
# i.e. {1 => [3], 2 => [3], 3 => [1;2]}
# to find if a graph is a cycle, check that each vertice has two edges
# this works because a single cycle graph will have exactly two edges from every vertice
# if there is any node outside of the cycle a node will have 3 edges
# if there is not a cycle at least two nodes will have 1 edge
# if there are multiple cycles, at least one node will have more than 2 edges
# this assumes a conencted graph, if the graph is not connected,
# then you can check at the end with a loop to make sure that you can reach every edge from any edge
# this check will not affect time complexity, but will add O(V) space for a visited list
# time complexity of O(V), one check at each vertices
# space complexity of O(1)

def detect_cycle graph:
    for i in range(0, len(graph))
        if len(graph[i]) != 2:
            return False
    return True
            
        