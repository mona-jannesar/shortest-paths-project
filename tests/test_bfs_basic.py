import pytest
from shorest_paths import bfs_shortest_path

def reconstruct_path(parent, goal):
    if goal not in parent:
        return None
    
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)
    return list(reversed(path))

def test_bfs_basic():
    graph = {
        'A': ['B'],
        'B': ['A', 'C'],     
        'C': ['B'],
    }
    
    distances, parent = bfs_shortest_path(graph, "A")
    assert distances ["A"] == 0
    assert distances ["B"] == 1
    assert distances ["C"] == 2 
    assert reconstruct_path(parent, "C") in (['A', 'B', 'C'],) # Only one shortest path exists

def test_bfs_disconnected():
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': [],
    }
    
    distances, parent = bfs_shortest_path(graph, "A")
    assert distances ["A"] == 0
    assert distances ["B"] == 1
    assert "C" not in distances
    assert "C" not in parent