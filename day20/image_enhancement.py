import numpy as np

def read_input(input_file):
    with open(input_file, 'r') as f:
        enhancer_algo = tuple(convert_picture_to_int_iter(next(f).strip()))
        lines = [list(convert_picture_to_int_iter(line))
                 for line in f.read().strip().splitlines()]
        img = np.array(lines, dtype=int)
        # Add a rim of zeros to simulate infinite img
        img = np.pad(img, 1)
        return enhancer_algo, img

def apply_multiple_enhancement_steps(img, enhancer_algo, steps, verbose=True):
    for step in range(1, steps+1):
        img = enhance_image(img, enhancer_algo)
        if verbose:
            print(f"Step {step}: {img.sum()} lit pixels")
    return img

def enhance_image(img, enhancer_algo, kernel_width=3):
    # Pad image with a full kernel width to simulate infinite image
    padded_img = np.pad(img, kernel_width, mode='edge')
    padding = kernel_width // 2
    result = np.zeros_like(padded_img, dtype=int)
    max_row, max_col = padded_img.shape
    for y in range(padding, max_row - padding):
        for x in range(padding, max_col - padding):
            window = padded_img[y-padding:y+padding+1, x-padding:x+padding+1]
            index = calc_index_from_window(window)
            result[y, x] = enhancer_algo[index]
    # Leave only the padding by which the image has really grown
    # i.e. a kernel of width 3 grows the image by 1 pixel on each side
    if kernel_width > 2:
        result = remove_padding(result, pad_width=kernel_width-padding)
    return result

def calc_index_from_window(window):
    binary_sequence = window.flatten()[::-1]
    return sum(n*2**i for i, n in enumerate(binary_sequence))

def convert_picture_to_int_iter(picture_string):
    translator = {'#': 1, '.': 0}
    return (translator.get(c, c) for c in picture_string)

def remove_padding(matrix, pad_width=1):
    return matrix[pad_width:-pad_width,pad_width:-pad_width]

if __name__ == '__main__':
    enhancer_algo, img = read_input('input.txt')
    final_img = apply_multiple_enhancement_steps(img, enhancer_algo, steps=50)
