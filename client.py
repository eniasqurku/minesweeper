from matrix import Matrix
from utils import format_matrix


class Client:

    def __init__(self, dimension=10):
        self.dimension = dimension
        self.view_matrix = self.create_view_matrix(dimension)
        self.m = Matrix(dimension)

    @staticmethod
    def create_view_matrix(dimension: int) -> list:
        matrix = []
        for i in range(dimension):
            row = []
            for j in range(dimension):
                row.append('-')
            matrix.append(row)

        return matrix

    def is_cleared(self) -> bool:
        cleared_cells = 0
        for i in self.view_matrix:
            for j in i:
                if isinstance(j, int):
                    cleared_cells += 1

        return cleared_cells == self.dimension ** 2 - self.m.nr_of_bombs

    def check(self, x: int, y: int) -> int:
        result = self.m.check(x, y)

        self.view_matrix[x][y] = result

        return result

    def __str__(self):
        return format_matrix(self.view_matrix)
