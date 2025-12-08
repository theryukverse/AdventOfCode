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
wires_available = 1000
top_n_clusters_size = 3


def get_distance(p1, p2):
    return (abs(p1.x - p2.x) ** 2 + abs(p1.y - p2.y) ** 2 + abs(p1.z - p2.z) ** 2) ** (
        1 / 2
    )


def get_min_coord(n2):
    row_index, col_index = np.unravel_index(np.argmin(n2), n2.shape)
    return row_index, col_index


def connect(points, distance, wires_available):
    while wires_available:
        p1_index, p2_index = get_min_coord(distance)
        points[p1_index].connect_points(points[p2_index])
        wires_available -= 1
        distance[p1_index][p2_index] = max_float
        distance[p2_index][p1_index] = max_float


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


def get_ans(points):
    clusters_sizes = []
    traversed_point_indexes = set()
    for i in range(len(points)):
        cluster, curr_traversed_point_indexes = get_cluster_with_point(
            i, points, traversed_point_indexes
        )
        traversed_point_indexes.update(curr_traversed_point_indexes)
        if cluster:
            clusters_sizes.append(len(cluster))
    top_n_clusters = sorted(clusters_sizes, reverse=True)[:top_n_clusters_size]
    ans = 1
    for s in top_n_clusters:
        ans *= s
    return ans


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
        connect(points, distance, wires_available)
        print(points)
        # print(distance)
        print(get_ans(points))
except FileNotFoundError:
    print("File not found")
