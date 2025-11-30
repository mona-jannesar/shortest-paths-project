from collections import deque
from typing import Dict, Tuple, Hashable, Optional
from .graph import unweightedGraph, Node

def bfs_shortest_path(graph: unweightedGraph, start: Node) -> Tuple[Dict[Node, int], Dict[Node, Optional[Node]]]:
    """
    Breadth-first search for shortest paths in an unweighted graph.

    Returns:
        dist[node]   = number of edges from start to node
        parent[node] = previous node on a shortest path from start
    """
    if start not in graph:
        raise ValueError (f"Start node {start!r} not in graph")
    
    distances: Dict[Node, int] = {start: 0}
    parent: Dict[Node, Optional[Node]] = {start: None}
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)

    return distances, parent