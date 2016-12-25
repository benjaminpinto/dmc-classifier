import math


def distance_euclid(origin, destiny):
    squared_distance = 0

    for i in range(0, len(origin)):
        squared_distance += math.pow((float(destiny[i]) - float(origin[i])), 2)

    distance = math.sqrt(squared_distance)

    return distance


def distance_manhattan(origin, destiny):
    pass