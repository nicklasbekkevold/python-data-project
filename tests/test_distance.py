import pytest

from .context import distance


@pytest.fixture
def X():
    return (0, 0)


@pytest.fixture
def Y():
    return (3, 4)


def test_manhattan_distance(X, Y):
    manhattan = distance.manhattan_distance(X, Y)
    assert manhattan == 7


def test_euclidean_distance(X, Y):
    euclidean = distance.euclidean_distance(X, Y)
    assert euclidean == 5


def test_minkowski_distance_manhattan_case(X, Y):
    manhattan = distance.manhattan_distance(X, Y)
    minkowski = distance.minkowski_distance(X, Y, p=1)

    assert minkowski == manhattan


def test_minkowski_distance_euclidean_case(X, Y):
    euclidean = distance.euclidean_distance(X, Y)
    minkowski = distance.minkowski_distance(X, Y, p=2)

    assert minkowski == euclidean
