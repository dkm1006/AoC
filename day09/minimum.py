from collections import deque
import numpy as np
import numpy.ma as ma

PADDING_VALUE = 10

def read_input(input_file):
    return np.genfromtxt(input_file, delimiter=1, dtype=int)

def sum_risk_levels(heightmap):
    min_values = get_local_minima(heightmap)
    return (heightmap[heightmap < min_values] + 1).sum()

def find_largest_basins(heightmap):
    basin_sizes = []
    basin_map = get_basin_map(heightmap)
    num_basins = basin_map.max()
    for basin_index in range(num_basins + 1):
        basin_size = np.count_nonzero(basin_map == basin_index)
        basin_sizes.append(basin_size)

    return sorted(basin_sizes, reverse=True)

def get_basin_map(heightmap):
    basin_map = np.zeros_like(heightmap)
    basin_map[heightmap == 9] = -1
    basin_map = pad(basin_map, constant_values=-1)
    basin_index = 0
    try:
        while next_zero := next(get_zero_coords(basin_map)):
            basin_index +=1
            basin_map = iter_basin(basin_map, basin_index, next_zero)
    except StopIteration as e:
        return remove_padding(basin_map)

def iter_basin(basin_map, basin_index, start_coords):
    candidates = set()
    candidates.add(start_coords)
    while len(candidates):
        candidate = candidates.pop()
        basin_map[candidate] = basin_index
        neighbours = get_neighbouring_zeros(basin_map, candidate)
        candidates |= set(neighbours)
    
    return basin_map

def get_local_minima(heightmap):
    min_values = heightmap.copy()
    padded_map = pad(heightmap)
    max_row, max_col = padded_map.shape
    neighbour_kernel = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    kernel_size = neighbour_kernel.shape[0]
    for row in range(0, max_row - kernel_size + 1):
        for col in range(0, max_col - kernel_size + 1):
            local_map = padded_map[row:row+kernel_size, col:col+kernel_size]
            neighbourhood = local_map[np.nonzero(neighbour_kernel)]
            min_values[row, col] = neighbourhood.min()
    
    return min_values

def get_zero_coords(basin_map):
    zero_coords = np.nonzero(basin_map == 0)
    return zip(*zero_coords)

def get_neighbouring_zeros(basin_map, current_coords):
    y0, x0 = current_coords
    neighbour_coords = (y0-1, y0, y0, y0+1), (x0, x0-1, x0+1, x0)
    mask = np.ones_like(basin_map) * -1
    mask[neighbour_coords] = basin_map[neighbour_coords]
    zero_coords = np.nonzero(mask == 0)
    return ((y, x) for y, x in zip(*zero_coords))

def pad(matrix, pad_width=1, mode='constant', constant_values=PADDING_VALUE):
    result = np.pad(
        matrix, [pad_width, pad_width],
        mode=mode, constant_values=constant_values
    )
    return result

def remove_padding(matrix, pad_width=1):
    return matrix[pad_width:-pad_width,pad_width:-pad_width]

if __name__ == '__main__':
    heightmap = read_input('input.txt')
    total_risk_level = sum_risk_levels(heightmap)
    print(f"Total risk level: {total_risk_level}")
    largest_basins = find_largest_basins(heightmap)[:3]
    result = np.prod(largest_basins)
    print(f"Product of largest basins: {result}")