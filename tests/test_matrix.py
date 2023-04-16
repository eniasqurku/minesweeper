import pytest

from cell import Cell
from matrix import Matrix


@pytest.fixture
def matrix():
    return Matrix(10)


def test_matrix_dimension(matrix):
    assert len(matrix.matrix) == 10
    assert len(matrix.matrix[0]) == 10


def test_matrix_is_comprised_of_cells(matrix):
    assert all([isinstance(column, Cell) for row in matrix.matrix for column in row])


def test_weight_matrix_is_comprised_of_integers(matrix):
    assert all([isinstance(column, int) for row in matrix.weight_matrix for column in row])


def test_check():
    mock_matrix = [
        [Cell('C', 0, 0, 3), Cell('C', 0, 1, 3), Cell('C', 0, 2, 3)],
        [Cell('B', 1, 0, 3), Cell('C', 1, 1, 3), Cell('C', 1, 2, 3)],
        [Cell('C', 2, 0, 3), Cell('C', 2, 1, 3), Cell('B', 2, 2, 3)],
    ]

    m = Matrix(3)
    m.matrix = mock_matrix

    assert m.check(0, 0) == 1
    assert m.check(1, 0) == -1
    assert m.check(2, 1) == 2
