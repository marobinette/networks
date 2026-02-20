def get_node_degree(adjacency_matrix: list[list[int]], node: int):
    row_index = node - 1
    row = adjacency_matrix[row_index]
    return row.count(1)

def get_highest_degree(adjacency_matrix: list[list[int]]):
    degrees = {
        node: get_node_degree(adjacency_matrix, node)
        for node in range(1, len(adjacency_matrix) + 1)
    }

    max_degree = max(degrees.values())

    return {    
        node: degree for node, degree in degrees.items() if degree == max_degree
    }


