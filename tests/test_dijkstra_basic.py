import pytest
from shortest_paths import dijkstra_shortest_path    

def reconstruct_path(parent, goal):
    if goal not in parent:
        return None
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)
    return list(reversed(path)) 

def test_dijkstra_small_weighted_graph():
    graph = {
        'A': [('B', 1), ('C', 1)],
        'B': [('D', 1)],
        'C': [('D', 100)],
        'D': [],
    }
    
    distances, parent = dijkstra_shortest_path(graph, "A")
    assert distances["D"] == pytest.approx(2.0)
    assert reconstruct_path(parent, "D") == ['A', 'B', 'D']

    def test_dijkstra_raises_0n_negative_edge():
        graph = {
            "A": [("B", -1)],
            "B": [],        
        }

        with pytest.raises(ValueError):
            dijkstra_shortest_path(graph, "A")
