import math


def manhattan_distance(X, Y):
    return sum([abs(x - y) for x, y in zip(X, Y)])


def euclidean_distance(X, Y):
    return math.sqrt(sum([(x - y) ** 2 for x, y in zip(X, Y)]))


def minkowski_distance(X, Y, p=2):
    return sum([abs(x - y) ** p for x, y in zip(X, Y)]) ** (1 / p)
