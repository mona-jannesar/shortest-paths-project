from typing import Dict, List, Tuple, Hashable

Node = Hashable
unweightedGraph = Dict[Node, List[Node]]
weightedGraph = Dict[Node, List[Tuple[Node, float]]]