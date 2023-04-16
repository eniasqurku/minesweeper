import pytest

from cell import Cell

data = [
    (Cell('', 0, 0, 10), [(0, 1), (1, 0), (1, 1)]),
    (Cell('', 9, 9, 10), [(9, 8), (8, 8), (8, 9)]),
    (Cell('', 0, 2, 10), [(0, 1), (0, 3), (1, 1), (1, 2), (1, 3)]),
    (Cell('', 1, 2, 10), [(0, 1), (0, 2), (0, 3), (1, 1), (1, 3), (2, 1), (2, 2), (2, 3)])
]


@pytest.fixture
def clear_cell():
    return Cell('C', 1, 1, 10)


@pytest.fixture
def bomb_cell():
    return Cell('B', 1, 1, 10)


@pytest.mark.parametrize("cell,coordinates", data)
def test_neighbours_coordinates(cell, coordinates):
    assert set(cell.neighbours_coordinates) == set(coordinates)


def test_is_bomb(clear_cell, bomb_cell):
    assert bomb_cell.is_bomb() is True
    assert clear_cell.is_bomb() is False


def test_weight_when_bomb(bomb_cell):
    neighbours = []

    assert bomb_cell.weight(neighbours) == 0


def test_weight_when_clear(clear_cell):
    neighbours = [
        Cell('C', 1, 1, 10),
        Cell('C', 1, 1, 10),
        Cell('B', 1, 1, 10),
        Cell('C', 1, 1, 10),
        Cell('B', 1, 1, 10),
    ]

    assert clear_cell.weight(neighbours) == 2
