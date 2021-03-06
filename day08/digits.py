from collections import Counter

CHARS = 'abcdefg'
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
# counts = Counter(''.join(NORMAL_ENCODED_DIGITS))
# OCCURRENCES2SEGMENT = {
#     count: key for key, count in counts.items()
#     if Counter(counts.values())[count] < 2
# }
OCCURRENCES2SEGMENT = {4: 'e', 6: 'b', 9: 'f'}
SEGMENT_MAP = {
    (0, 1, 2, 4, 5, 6): 0,
    (2, 5): 1,
    (0, 2, 3, 4, 6): 2,
    (0, 2, 3, 5, 6): 3,
    (1, 2, 3, 5): 4,
    (0, 1, 3, 5, 6): 5,
    (0, 1, 3, 4, 5, 6): 6,
    (0, 2, 5): 7,
    (0, 1, 2, 3, 4, 5, 6): 8,
    (0, 1, 2, 3, 5, 6): 9
}
ONE_HOT_SEGMENT_MAP = {
    (1, 1, 1, 0, 1, 1, 1): 0,
    (0, 0, 1, 0, 0, 1, 0): 1,
    (1, 0, 1, 1, 1, 0, 1): 2,
    (1, 0, 1, 1, 0, 1, 1): 3,
    (0, 1, 1, 1, 0, 1, 0): 4,
    (1, 1, 0, 1, 0, 1, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (1, 0, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 1, 1, 1, 1): 8,
    (1, 1, 1, 1, 0, 1, 1): 9,
}

def read_input(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            signal_patterns, output = line.split(' | ')
            yield (signal_patterns.split(), output.split())

def count_1478(display_values):
    length_set = {2, 3, 4, 7}
    counter = 0
    for signal_patterns, output in display_values:
        counter += sum(
            1 for signal in output if len(signal) in length_set
        )
    
    return counter

def sum_outputs(display_values):
    """The result is the sum of all output values"""
    accumulator = 0
    for signal_patterns, output in display_values:
        translator = create_translator(signal_patterns)
        number = decode_number(output, translator)
        # print(f"{' '.join(output)}: {number}")
        accumulator += number

    return accumulator

def create_translator(signal_patterns):
    translation_table = {}
    segment_counts = Counter(''.join(signal_patterns))
    # Only the unique signal_lengths are interesting, so we can overwrite
    # those that occur twice
    signal_lengths = {len(signal): signal for signal in signal_patterns}
    for char, occurrences in segment_counts.items():
        if occurrences in OCCURRENCES2SEGMENT:
            translation_table[char] = OCCURRENCES2SEGMENT[occurrences]
        elif occurrences == 7:
            if char in signal_lengths[4]:
                translation_table[char] = 'd'
            else: 
                translation_table[char] = 'g'
        elif occurrences == 8:
            if char in signal_lengths[2]:
                translation_table[char] = 'c'
            else: 
                translation_table[char] = 'a'

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

def char2index(char):
    """Returns ord(char) - ord('a')"""
    return ord(char) - 97

def one_hot(indexes):
    return tuple(1 if i in indexes else 0 for i in range(7))

def look_at_digits():
    for digit in NORMAL_ENCODED_DIGITS:
        indexes = tuple(char2index(char) for char in digit)
        one_hot_encoded = one_hot(indexes)
        result = SEGMENT_MAP[one_hot_encoded]
        print(' --> '.join((digit, str(indexes), str(one_hot_encoded), str(result))))


if __name__ == '__main__':
    display_values = list(read_input('input.txt'))
    result_part1 = count_1478(display_values)
    result_part2 = sum_outputs(display_values)
    print(f"Result Part 1: {result_part1}")
    print(f"Result Part 2: {result_part2}")

