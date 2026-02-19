from src.networks import *

matrix = [
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
]

def test_get_node_degree():
    assert get_node_degree(matrix, 3) == 4