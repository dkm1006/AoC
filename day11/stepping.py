import numpy as np

FLASH_THRESHOLD = 9
NEIGHBOURS = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=int)

def read_input(input_file):
    return np.genfromtxt(input_file, delimiter=1, dtype=int)

def simulate_cave(energymap, max_steps=1000):
    h,w = energymap.shape
    total_octopuses = h*w
    total_flashes = 0
    for step in range(1, max_steps+1):
        energymap = step_fn(energymap)
        num_flashes = (energymap == 0).sum()
        total_flashes += num_flashes
        print(f"Step {step}: {num_flashes} flashes (Total: {total_flashes})")
        if num_flashes == total_octopuses:
            first_sync_step = step
            print(f"Step {step}: Octopus flashing has synced")
            break
    else:
        print(f"No flash syncing occurred within {max_steps} steps")
        first_sync_step = None
    
    return total_flashes, first_sync_step

def step_fn(energymap):
    energymap += 1
    flashmap = (energymap > FLASH_THRESHOLD).astype(int)
    new_flashes = flashmap.copy()
    while new_flashes.any():
        energymap += convolve2d(new_flashes, NEIGHBOURS)
        new_flashes = (energymap > FLASH_THRESHOLD).astype(int) - flashmap
        flashmap += new_flashes

    energymap[flashmap.astype(bool)] = 0
    return energymap

def convolve2d(matrix, kernel):
    padding = kernel.shape[0] // 2
    padded_map = np.pad(matrix, padding)
    result = np.zeros_like(matrix)
    max_row, max_col = padded_map.shape
    for y in range(padding, max_row - padding):
        for x in range(padding, max_col - padding):
            window = padded_map[y-padding:y+padding+1, x-padding:x+padding+1]
            convolved = (window * kernel).sum()
            result[y-padding, x-padding] = convolved

    return result

if __name__ == '__main__':
    energymap = read_input('input.txt')
    total_flashes, first_sync_step = simulate_cave(energymap)
    print(f"Total # flashes: {total_flashes}")
    print(f"First sync step: {first_sync_step}")
