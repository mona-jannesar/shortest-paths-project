import heapq
from typing import Dict, Tuple, Hashable, Optional
from .graph import weightedGraph, Node  
def dijkstra_shortest_path(graph: weightedGraph, start: Node) -> Tuple[Dict[Node, float], Dict[Node, Optional[Node]]]:
    """
    Find the shortest path in a weighted graph using Dijkstra's algorithm.

    :param graph: A weighted graph represented as an adjacency list with edge weights.
    :param start: The starting node.
    :param goal: The goal node.
    :return: A tuple containing two dictionaries:
             dist[node]   = minimumtotal weight from start to node
             parent[node] = previous node on a shortest path from start  
    """
    if start not in graph:
        raise ValueError(f"Start node {start!r} not in graph")
    
    distances: Dict[Node, float] = {start: 0.0}
    parent: Dict[Node, Optional[Node]] = {start: None}
    priority_queue = [(0.0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances.get(current_node, float('inf')):
            continue

        for neighbor, weight in graph.get(current_node, []):
            if weight < 0:
                raise ValueError("Graph contains negative weight edge, which is not allowed in Dijkstra's algorithm")
            
            new_distance = current_distance + weight

            if neighbor not in distances or new_distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_distance
                parent[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, parent