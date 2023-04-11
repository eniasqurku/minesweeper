class Cell:

    def __init__(self, type: str, row: int, column: int, dimension: int):
        self.type = type
        self.row = row
        self.column = column
        self.dimension = dimension

    @property
    def coordinates(self) -> tuple:
        return self.row, self.column

    def weight(self, neighbours: list) -> int:
        return neighbours.count('B') if self.type == 'C' else 0

    @property
    def neighbours_coordinates(self) -> list:
        y_range = [self.row - 1, self.row, self.row + 1]
        y_range = [y for y in y_range if y >= 0 and y < self.dimension]

        x_range = [self.column - 1, self.column, self.column + 1]
        x_range = [x for x in x_range if x >= 0 and x < self.dimension]

        coordinates = []

        for y in y_range:
            for x in x_range:
                if y == self.row and x == self.column:
                    continue

                coordinates.append((y, x))

        return coordinates

    def is_bomb(self) -> bool:
        return self.type == 'B'

    def __str__(self):
        return self.type

    def __repr__(self):
        return self.type

    def __format__(self, format_spec):
        return self.type.__format__(format_spec)

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.type == other.type
        elif isinstance(other, str):
            return self.type == other

        return False
