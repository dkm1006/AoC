import numpy as np
from ..util  import timing

CHARS = 'abcdefg'
CHARS_DICT = {char: index for index, char in enumerate(CHARS)}
NORMAL_ENCODED_DIGITS = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

def read_input(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            signal_patterns, output = line.split(' | ')
            yield (signal_patterns.split(), output.split())

@timing
def sum_outputs(display_values):
    """The result is the sum of all output values"""
    normed_table = create_lookup_table(signal_patterns=NORMAL_ENCODED_DIGITS)
    accumulator = 0
    for signal_patterns, output in display_values:
        translator = create_translator(signal_patterns, normed_table)
        number = decode_number(output, translator)
        # print(f"{' '.join(output)}: {number}")
        accumulator += number

    return accumulator

def create_lookup_table(signal_patterns):
    normed_cooccurrences = find_cooccurrences(signal_patterns)
    keys = calculate_features(normed_cooccurrences)
    return {k: v for k, v in zip(keys, CHARS)}

def create_translator(signal_patterns, normed_table):
    encoded_table = create_lookup_table(signal_patterns)
    translation_table = {
        char: normed_table[feature] for feature, char in encoded_table.items()
    }
    return str.maketrans(translation_table)

def decode_number(output, translator):
    digits = []
    for encoded in output:
        translated = encoded.translate(translator)
        # indexes = tuple(char2index(char) for char in sorted(translated))
        digit = str(NORMAL_ENCODED_DIGITS[''.join(sorted(translated))])
        digits.append(digit)
        
    number = int(''.join(digits))
    return number

# def find_cooccurrences(signal_patterns):
#     # cooccurrences = defaultdict(lambda: defaultdict(lambda: 0))
#     cooccurrences = np.zeros((7, 7), dtype=int)
#     for i, char in enumerate(CHARS):
#         for j, other_char in enumerate(CHARS):
#             for encoded in signal_patterns:
#                 if char in encoded and other_char in encoded:
#                     cooccurrences[i][j] += 1
    
#     return cooccurrences

def find_cooccurrences(signal_patterns):
    cooccurrences = np.zeros((7, 7), dtype=int)
    for pattern in signal_patterns:
        for char in pattern:
            i = CHARS[char]
            for other_char in pattern:
                j = CHARS[other_char]
                cooccurrences[i][j] += 1

    return cooccurrences

def calculate_features(cooccurrences):
    totals = cooccurrences.sum(axis=0)
    medians = np.median(cooccurrences, axis=0).astype(int)
    return totals + medians


if __name__ == '__main__':
    display_values = list(read_input('input.txt'))
    # result_part1 = count_1478(display_values)
    result_part2 = sum_outputs(display_values)
    # print(f"Result Part 1: {result_part1}")
    print(f"Result Part 2: {result_part2}")

