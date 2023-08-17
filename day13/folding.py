import numpy as np

def read_input(input_file):
    with open(input_file, 'r') as f:
        dots = []
        fold_instructions = []
        is_fold_instruction = False
        for line in f.readlines():
            if not line.strip():
                is_fold_instruction = True
                continue
            elif is_fold_instruction:
                axis, coord = line.split('=')
                fold_instructions.append((axis[-1], int(coord)))
            else:
                x, y = line.split(',')
                dots.append((x, y))

    dots = np.array(dots, dtype=int)
    max_coord = dots.max() + 1
    dotmap = np.zeros((max_coord, max_coord))
    dotmap[dots[:, 1], dots[:, 0]] = 1
    return dotmap, fold_instructions

def fold(matrix, instruction):
    axis, coord = instruction
    result = matrix.T if 'x' in axis else matrix
    diff = coord - result.shape[0] // 2
    lower_end = max(0, diff)
    upper_end = result.shape[0] + 2*diff
    flipped = np.flipud(result[coord+1:upper_end, :])
    result[lower_end:coord, :] += flipped
    result = result[:coord, :]
    return result.T if 'x' in axis else result

def show_dotmap(dotmap):
    output = []
    for row in dotmap:
        output.append(''.join(['#' if cell else ' ' for cell in row]))

    return '\n'.join(output)

if __name__ == '__main__':
    dotmap, fold_instructions = read_input('input.txt')
    for instruction in fold_instructions:
        dotmap = fold(dotmap, instruction)
        print(f"Visible dots: {dotmap.astype(bool).sum()}")
    
    print(show_dotmap(dotmap))

