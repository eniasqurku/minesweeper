def format_matrix(matrix: list) -> str:
    return '\n'.join(['   '.join([str(item) for item in row]) for row in matrix])
