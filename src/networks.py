def get_node_degree(adjacency_matrix: list[list[int]], node: int):
    row_index = node - 1
    row = adjacency_matrix[row_index]
    return row.count(1)