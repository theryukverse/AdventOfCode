import numpy as np
import sys


class Point:
    def __init__(self, x=0, y=0, z=0, id=-1):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.children = set()

    def connect_points(self, another_point):
        self.add_child(another_point)
        another_point.add_child(self)

    def add_child(self, another_point):
        self.children.add(another_point)


max_float = sys.float_info.max


def get_distance(p1, p2):
    return (abs(p1.x - p2.x) ** 2 + abs(p1.y - p2.y) ** 2 + abs(p1.z - p2.z) ** 2) ** (
        1 / 2
    )


def get_min_coord(n2):
    row_index, col_index = np.unravel_index(np.argmin(n2), n2.shape)
    return row_index, col_index


def get_cluster_with_point(point_index, points, traversed_point_indexes):
    point = points[point_index]
    if point.id in traversed_point_indexes:
        return set(), set()
    traversed_point_indexes.add(point.id)
    cluster = {point.id}

    if len(point.children):
        for c in point.children:
            curr_cluster, curr_traversed_point_indexes = get_cluster_with_point(
                c.id, points, traversed_point_indexes
            )
            cluster.update(curr_cluster)
            traversed_point_indexes.update(curr_traversed_point_indexes)
    return cluster, traversed_point_indexes


def connect(points, distance):
    last_connection = []
    while len(get_cluster_with_point(0, points, set())[0]) != len(points):
        p1_index, p2_index = get_min_coord(distance)
        points[p1_index].connect_points(points[p2_index])
        last_connection = [p1_index, p2_index]
        distance[p1_index][p2_index] = max_float
        distance[p2_index][p1_index] = max_float
    return points[last_connection[0]].x * points[last_connection[1]].x


try:
    points = []
    with open("input/Day 8 Playground.txt", "r") as file:
        for line in file:
            point = line.strip().split(",")
            points.append(
                Point(int(point[0]), int(point[1]), int(point[2]), len(points))
            )
        num_of_points = len(points)
        distance = np.zeros((num_of_points, num_of_points))
        for i in range(num_of_points):
            for j in range(num_of_points):
                if i == j:
                    distance[i][j] = max_float
                    continue
                distance[i][j] = get_distance(points[i], points[j])
                distance[j][i] = distance[i][j]
        print(points)
        print(distance)
        print(connect(points, distance))
except FileNotFoundError:
    print("File not found")
