import numpy as np

def read_input(input_file):
    with open(input_file, 'r') as f:
        lines = [
            tuple(convert_picture_to_int_iter(line))
            for line in f.read().strip().splitlines()
        ]
    img = np.array(lines, dtype=int)
    return img

def convert_picture_to_int_iter(picture_string):
    translator = {'.': 0, '>': 1, 'v':2}
    return (translator.get(c, c) for c in picture_string)

def simulate_migration(img, should_show_map=False):
    step = 0
    num_moved = 1
    if should_show_map:
        print(show_map(img))
    while num_moved > 0:
        img, num_moved_east = move(img, choice=1)
        img, num_moved_south = move(img, choice=2)
        num_moved = num_moved_east + num_moved_south
        step += 1
        print(f"Step {step}: {num_moved} cucumbers moved")
        if should_show_map:
            print(show_map(img))
    return step

def move(img, choice):
    """
    Swaps all positions of value choice with a free (0) position to the
    east (choice=1) or south (choice=2)
    Returns the img and the number of changes positions
    """
    get_target_pos = {
        1: next_east,
        2: next_south
    }
    correctly_facing = np.nonzero(img == choice)
    target_positions = get_target_pos[choice](correctly_facing)
    mask = (img == 0)[target_positions]
    moving_positions = apply_coordinate_mask(correctly_facing, mask)
    empty_positions = apply_coordinate_mask(target_positions, mask)
    img[moving_positions] = 0
    img[empty_positions] = choice
    return img, len(moving_positions[0])

def next_east(coords):
    return (coords[0], (coords[1] + 1) % img.shape[1])

def next_south(coords):
    return (coords[0] + 1) % img.shape[0], coords[1]

def apply_coordinate_mask(coords, mask):
    """
    Filters a tuple of coords with an array of same len with boolean entries
    """
    return coords[0][mask], coords[1][mask]

def show_map(img):
    translator = {0:'.', 1:'>', 2:'v'}
    output = []
    for row in img:
        output.append(''.join([translator.get(cell, cell) for cell in row]))
    return '\n'.join(output)

if __name__ == '__main__':
    img = read_input('test_input.txt')
    num_steps = simulate_migration(img)
