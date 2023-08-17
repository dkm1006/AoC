import math
import re
from itertools import combinations, permutations, tee
import numpy as np

HEADLINE_PATTERN = r"-+ scanner (\d+) -+"

def parse_scanner_report(file_input):
    """
    Reads the file at file_input and 
    returns a list of lists of relative beacon coordinates
    """
    with open(file_input, 'r') as f:
        lines = f.read().splitlines()
    scanners = []
    for line in lines:
        headline_match = re.match(HEADLINE_PATTERN, line)
        if headline_match:
            scanners.append([])
            beacon_list = scanners[-1]
            index = headline_match[1]
            print(f"Parsing scanner {index}")
        elif line:
            coords = np.array([int(c) for c in line.split(',')])
            beacon_list.append(coords)
    return scanners

def construct_beacon_map(scanners):
    pass




def get_transformation_matrices():
    UNIT_VECTORS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    UNIT_PERMUTATIONS = tuple(permutations(UNIT_VECTORS))
    transformation_matrices = [np.matrix(p) for p in UNIT_PERMUTATIONS]
    mirrored_matrices = []
    for m in transformation_matrices:
        for start in range(3):
            mirrored = m.copy()
            mirrored[start] *= -1
            mirrored_matrices.append(mirrored)
    transformation_matrices.extend(mirrored_matrices)
    return transformation_matrices

def compare_scanners_pairwise(scanners):
    for scanner, other_scanner in pairwise(scanners):
        pass

def get_triplets(beacon_list):
    for triplet in combinations(beacon_list, 3):
        midpoint = get_midpoint(triplet)
        # normed_coords = get_coords_from_midpoint(triplet)
        moment = calculate_moment(triplet)
    
    # If two triplets from different scanners have identical moments, they include the same beacons
    # Should be a tetrahedron?
    # Compare distances, find midpoint
    # Midpoint is known 
    # T@R@v = v'

def compare_distances(scanners, transformation_matrices):
    for scanner, other_scanner in combinations(scanners, 2):
        distances = get_distances(scanner)
        other_distances = get_distances(other_scanner)
        for distance in distances:
            if distance in other_distances:
                pair = distances[distance]
                other_pair = other_distances[distance]
                print(f"Found identical distance for {pair}, {other_pair}")
                normed_coords = get_coords_from_midpoint(pair)
                other_normed_coords = get_coords_from_midpoint(other_pair)
                for transformation in transformation_matrices:
                    transformed_coords = tuple(transform(v, transformation) for v in other_normed_coords)
                    diff = tuple(t - c for t, c in zip(transformed_coords, normed_coords))
                    print(pair, other_pair)
                    print(normed_coords, other_normed_coords)
                    print(transformed_coords)
                    print(diff)
                    break


def transform(vector, transformation):
    return transformation @ vector

def get_distances(beacon_list, rounding=4):
    distance_map = {}
    for beacon, other_beacon in combinations(beacon_list, 2):
        distance = round(calculate_distance(beacon, other_beacon), rounding)
        if distance in distance_map:
            print(f"Same distance {distance}:")
            print(beacon, other_beacon)
            print(*distance_map[distance])
        distance_map[distance] = (beacon, other_beacon)
    return distance_map

def get_coords_from_midpoint(beacon_pair):
    beacon, other_beacon = beacon_pair
    midpoint = (other_beacon - beacon) / 2
    return beacon - midpoint, other_beacon - midpoint


def calculate_distance(a, b):
    diff = b - a
    return np.sqrt(diff @ diff)

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

if __name__ == '__main__':
    scanners = parse_scanner_report('test_input.txt')
    transformation_matrices = get_transformation_matrices()





##################### OLD #############

DISCRETE_ROTATION_ANGLES = (np.pi/2, np.pi, 3*np.pi/2)
IDENTITY_MATRIX = np.matrix(np.eye(3, dtype=int))

def get_transformation_matrices():
    transformation_matrices = [IDENTITY_MATRIX]
    # Elementary rotations:
    for angle in DISCRETE_ROTATION_ANGLES:
        rx = x_rotation_matrix(angle)
        ry = y_rotation_matrix(angle)
        rz = z_rotation_matrix(angle)
        transformation_matrices.extend((rx, ry, rz))

    return transformation_matrices

def get_elementary_rotation_matrices():
    transformation_matrices = [IDENTITY_MATRIX]
    # Elementary rotations:
    for angle in DISCRETE_ROTATION_ANGLES:
        rx = x_rotation_matrix(angle)
        ry = y_rotation_matrix(angle)
        rz = z_rotation_matrix(angle)
        transformation_matrices.extend((rx, ry, rz))

    return transformation_matrices

def x_rotation_matrix(angle):
    rotation_matrix = np.matrix(
        [[1, 0, 0],
         [0, np.cos(angle), -np.sin(angle)],
         [0, np.sin(angle), np.cos(angle)]]
    )
    return rotation_matrix.astype(int)

def y_rotation_matrix(angle):
    rotation_matrix = np.matrix(
        [[np.cos(angle), 0, np.sin(angle)],
         [0, 1, 0],
         [-np.sin(angle), 0, np.cos(angle)]]
    )
    return rotation_matrix.astype(int)

def z_rotation_matrix(angle):
    rotation_matrix = np.matrix(
        [[np.cos(angle), -np.sin(angle), 0],
         [np.sin(angle), np.cos(angle), 0],
         [0, 0, 1]]
    )
    return rotation_matrix.astype(int)

def get_mirror_matrices():
    mirror_matrices = []
    for axis in (0, 1, 2):
        mirror_matrix = IDENTITY_MATRIX.copy()
        mirror_matrix[axis] *= -1
        mirror_matrices.append(mirror_matrix)
    return mirror_matrices

############