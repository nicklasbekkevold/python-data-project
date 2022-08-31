import pytest

from .context import distance


@pytest.fixture
def x():
    return (0, 0)


@pytest.fixture
def y():
    return (3, 4)


def test_manhattan_distance(x, y):
    d_manhattan = distance.manhattan_distance(x, y)
    assert d_manhattan == 7


def test_euclidean_distance(x, y):
    d_euclidean = distance.euclidean_distance(x, y)
    assert d_euclidean == 5


def test_minkowski_distance_manhattan_case(x, y):
    d_manhattan = distance.manhattan_distance(x, y)
    d_minkowski = distance.minkowski_distance(x, y, p=1)

    assert d_minkowski == d_manhattan


def test_minkowski_distance_euclidean_case(x, y):
    d_euclidean = distance.euclidean_distance(x, y)
    d_minkowski = distance.minkowski_distance(x, y, p=2)

    assert d_minkowski == d_euclidean
