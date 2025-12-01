import random
import time
import pytest

from shortest_paths import bfs_shortest_path, dijkstra_shortest_path
from shortest_paths.dijkstra import dijkstra_shortest_path

def generate_random_unweighted_graph(n_nodes=2000, avg_degree=5):
    nodes = list(range(n_nodes))
    graph = {u: [] for u in nodes}
    for u in nodes:
        for _ in range(avg_degree):
            v = random.randint(0, n_nodes - 1)
            if v != u:
                graph[u].append(v)
    return graph

def generate_random_weighted_graph(n_nodes=2000, avg_degree=5):
    nodes = list(range(n_nodes))
    graph = {u: [] for u in nodes}
    for u in nodes:
        for _ in range(avg_degree):
            v = random.randint(0, n_nodes - 1)
            if v != u:
                w = random.uniform(0.1, 10.0)
                graph[u].append((v, w))
    return graph

@pytest.mark.slow
def test_bfs_performance():
    graph = generate_random_unweighted_graph()
    start = 0
    t0 = time.perf_counter()
    dist, parent = bfs_shortest_path(graph, start)
    t1 = time.perf_counter()
    elapsed = t1 - t0
    # Loose bound; adjust as needed
    assert elapsed < 0.5, f"BFS too slow: {elapsed:.3f}s"

@pytest.mark.slow
def test_dijkstra_performance():
    graph = generate_random_weighted_graph()
    start = 0
    t0 = time.perf_counter()
    dist, parent = dijkstra_shortest_path(graph, start)
    t1 = time.perf_counter()
    elapsed = t1 - t0
    # Loose bound; adjust as needed
    assert elapsed < 1.0, f"Dijkstra too slow: {elapsed:.3f}s"
