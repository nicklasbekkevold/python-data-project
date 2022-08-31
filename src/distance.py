import math


def manhattan_distance(x, y):
    return sum([abs(x_i - y_i) for x_i, y_i in zip(x, y)])


def euclidean_distance(x, y):
    return math.sqrt(sum([(x_i - y_i) ** 2 for x_i, y_i in zip(x, y)]))


def minkowski_distance(x, y, p=2):
    return sum([abs(x_i - y_i) ** p for x_i, y_i in zip(x, y)]) ** (1 / p)
