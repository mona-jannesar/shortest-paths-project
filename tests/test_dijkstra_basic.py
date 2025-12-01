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

def path_cost(path, graph):
    """Compute total cost along a path for a weighted adjacency list graph."""
    if path is None:
        return None
    total = 0.0
    for u, v in zip(path, path[1:]):
        for nbr, w in graph[u]:
            if nbr == v:
                total += w
                break
        else:
            raise ValueError(f"No edge {u} -> {v} in graph")
    return total


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
# ---------- Numerical stability tests ----------

def test_dijkstra_float_rounding_stability():
    """
    Numerical stability check:
    0.1 + 0.2 should be treated as ≈ 0.3, not compared with exact equality.
    Both A->B->C and A->C have theoretical cost 0.3.
    """
    graph = {
        "A": [("B", 0.1), ("C", 0.3)],
        "B": [("C", 0.2)],
        "C": [],
    }

    distances, parent = dijkstra_shortest_path(graph, "A")
    path = reconstruct_path(parent, "C")
    cost = path_cost(path, graph)

    # Check that the distance is approximately 0.3
    assert distances["C"] == pytest.approx(0.3, rel=1e-9, abs=1e-12)
    # And that the stored distance matches the actual path cost
    assert cost == pytest.approx(distances["C"], rel=1e-9, abs=1e-12)


def test_dijkstra_distance_matches_path_sum():
    """
    For every reachable node, dist[node] should match
    the sum of weights along the reconstructed shortest path (within tolerance).
    This is a self-consistency / numerical-stability check.
    """
    graph = {
        0: [(1, 1.5), (2, 2.0)],
        1: [(3, 2.5)],
        2: [(3, 1.4)],
        3: [],
    }

    distances, parent = dijkstra_shortest_path(graph, 0)

    for node, d in distances.items():
        path = reconstruct_path(parent, node)
        cost = path_cost(path, graph)
        assert cost == pytest.approx(d, rel=1e-9, abs=1e-12)