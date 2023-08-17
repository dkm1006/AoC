from itertools import chain, product, tee
from functools import reduce
import re

def read_instructions(input_file):
    """
    Reads the input_file and returns a list of instructions which consist
    of a (command, cube) tuple
    """
    RANGE_PATTERN = r"(-?\d+)\.+(-?\d+)"
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    
    instructions = []
    for line in lines:
        command = line.startswith('on')
        ranges = tuple(
            (int(start), int(end)+1) for start, end 
            in re.findall(RANGE_PATTERN, line)
        )
        instructions.append((command, ranges))
    return instructions

def initialize_cube_reactor(instructions):
    current_cubes = []
    for index, (command, cube) in enumerate(instructions):
        print(f"{index}: Setting {command} for {cube}")
        new_cubes = [cube] if command else []
        for other_cube in current_cubes:
            combined_cubes = combine_cubes(other_cube, cube)
            new_cubes.extend(combined_cubes)
        
        current_cubes = new_cubes
    return current_cubes

def combine_cubes(old_cube, new_cube):
    intersection_cube = intersect_cubes(old_cube, new_cube)
    if intersection_cube:
        slices = slice_cube(old_cube, intersection_cube)
        resulting_cubes = slices
    else:
        resulting_cubes = [old_cube]
    return resulting_cubes

def intersect_cubes(cube, other_cube):
    # cubes are defined by their ranges
    edges = (
        intersect_edges(edge, other_edge)
        for edge, other_edge
        in zip(cube, other_cube)
    )
    intersection_cube = tuple(
        (start, end) for start, end in edges if end - start >= 0
    )
    return intersection_cube if len(intersection_cube) == 3 else tuple()

def slice_cube(cube, intersection_cube):
    edges = tuple(
        tuple(pairwise(sorted(set(chain(cube_edge, intersection_edge)))))
        for cube_edge, intersection_edge in zip(cube, intersection_cube)
    )
    return [
        new_cube for new_cube in product(*edges)
        if not new_cube == intersection_cube
    ]

def intersect_edges(edge, other_edge):
    return (max(edge[0], other_edge[0]), min(edge[1], other_edge[1]))

def clip_ranges(ranges, min_start=-50, max_end=51):
    return tuple(
        (max(start-min_start, 0), min(max(end-min_start, 0), max_end-min_start))
        for start, end in ranges
    )

def size(cuboid):
    side_lengths = (len(range(start, end)) for start, end in cuboid)
    return reduce(lambda c, n: c*n, side_lengths)

# def size(cuboid):
#     side_lengths = (end - start for start, end in cuboid)
#     return reduce(lambda c, n: c*n, side_lengths)

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

if __name__ == '__main__':
    instructions = read_instructions('input.txt')
    # reactor = initialize_reactor(instructions, min_start=-50, max_end=51)
    # reactor = initialize_sparse_reactor(instructions, min_start=-50, max_end=51)
    reactor = initialize_cube_reactor(instructions)
    clipped = (clip_ranges(c, min_start=-50, max_end=51) for c in reactor)
    print(f"Part 1: {sum(size(c) for c in clipped)} cubes are lit")
    print(f"Part 2: {sum(size(c) for c in reactor)} cubes are lit")




# import numpy as np
# 
# def offset_ranges(instructions, min_coord):
#     min_coord, max_coord = 0, 0
#     min_coord, max_coord = find_min_max(ranges, min_coord, max_coord)
#     offset_instructions = []
#     for command, ranges in instructions:
#         new_ranges = tuple(
#             (start-min_coord, end-min_coord) for start, end in ranges
#         )
#         print(ranges, '---', new_ranges)
#         offset_instructions.append((command, new_ranges))
#     return offset_instructions

# def find_min_max(ranges, current_min, current_max):
#     min_coord = min(chain(*ranges))
#     result_min = min_coord if min_coord < current_min else current_min
#     max_coord = max(chain(*ranges))
#     result_max = max_coord if max_coord > current_max else current_max
#     return result_min, result_max

# def initialize_reactor(instructions, min_start, max_end):
#     cuboid_shape = (max_end-min_start-1, ) * 3
#     reactor_cuboid = np.zeros(cuboid_shape, dtype=bool)
#     for command, ranges in instructions:
#         print(f"{reactor_cuboid.sum()} cubes are on")
#         print(f"Instruction: {command} for {ranges}")
#         clipped_ranges = clip_ranges(ranges)
#         print(f"Clipped ranges: {clipped_ranges}")
#         (x_start, x_end), (y_start, y_end), (z_start, z_end) = clipped_ranges
#         print(reactor_cuboid[x_start:x_end, y_start:y_end, z_start:z_end].shape)
#         reactor_cuboid[x_start:x_end, y_start:y_end, z_start:z_end] = command
    
#     print(f"{reactor_cuboid.sum()} cubes are on")
#     return reactor_cuboid


# def initialize_sparse_reactor(instructions, min_start, max_end):
#     """
#     Initializes a sparse reactor with many non active areas
#     """
#     # reactor holds the set of active cubes
#     reactor = set()
#     for index, (command, ranges) in enumerate(instructions):
#         clipped_ranges = clip_ranges(ranges, min_start, max_end)
#         print(f"{index}: Setting {command} for {clipped_ranges}")
#         coords_iter = (tuple(i for i in range(start, end)) for start, end in clipped_ranges)
#         cuboid = set(product(*coords_iter))
#         # reactor = reactor.union(cuboid) if command else reactor.difference(cuboid)
#         reactor = reactor | cuboid if command else reactor - cuboid
#     return reactor

