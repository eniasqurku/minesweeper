from random import randint

from cell import Cell
from utils import format_matrix


class Matrix:

    def __init__(self, dimension=10):
        self.dimension = dimension
        self.matrix, self.nr_of_bombs = self.create_matrix(dimension)
        self.weight_matrix = self.create_weight_matrix()

    def get_neighbours(self, coordinates: list) -> list:
        return [self.matrix[x][y] for x, y in coordinates]

    def get_weight(self, cell: Cell) -> int:
        neighbours = self.get_neighbours(cell.neighbours_coordinates)

        return cell.weight(neighbours)

    def create_weight_matrix(self) -> list:
        weight_matrix = []
        for row in self.matrix:
            row_data = []
            for cell in row:
                weight = self.get_weight(cell)
                row_data.append(weight)

            weight_matrix.append(row_data)

        return weight_matrix

    def print_weight_matrix(self) -> None:
        print(format_matrix(self.weight_matrix))

    @staticmethod
    def create_matrix(dimension: int) -> tuple[list, int]:
        matrix = []
        nr_of_bombs = 0
        for i in range(dimension):
            row = []
            for j in range(dimension):
                rand = randint(0, 4)
                if rand == 0:
                    row.append(Cell('B', i, j, dimension))
                    nr_of_bombs += 1
                else:
                    row.append(Cell('C', i, j, dimension))
            matrix.append(row)

        return matrix, nr_of_bombs

    def check(self, x: int, y: int) -> int:
        cell = self.matrix[x][y]
        if cell.is_bomb():
            return -1

        return self.get_weight(cell)

    def __str__(self):
        return format_matrix(self.matrix)
