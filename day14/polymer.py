import numpy as np
from collections import Counter


def read_input(input_file):
    with open(input_file, 'r') as f:
        initial_pairs = [a+b for a, b in iter_pairs(next(f).strip())]
        insertion_rules = {}
        for line in f.read().strip().splitlines():
            pair, insertion = line.split(' -> ')
            insertion_rules[pair] = (pair[0] + insertion, insertion + pair[1])

    indices = {pair: index for index, pair in enumerate(insertion_rules)}
    integer_insertion_rules = {
        indices[pair_before]: (indices[pair_left], indices[pair_right])
        for pair_before, (pair_left, pair_right)
        in insertion_rules.items()
    }
    initial_pair_vec = initialize_pair_vec(initial_pairs, indices)
    return initial_pair_vec, indices, integer_insertion_rules


def initialize_pair_vec(initial_pairs, indices):
    counts = Counter(initial_pairs)
    pair_vec = [0] * len(indices)
    for pair, count in counts.items():
        pair_vec[indices[pair]] = count
    
    return pair_vec

def iter_pairs(sequence):
    yield from zip(sequence[:-1], sequence[1:])

def simulate_polymerization(pair_vec, integer_insertion_rules, steps=10):
    for step in range(steps):
        pair_vec = apply_insertion_rules(pair_vec, integer_insertion_rules)
    
    return pair_vec

def apply_insertion_rules(pair_vec, integer_insertion_rules):
    result_vec = pair_vec[:]
    for index, num_pairs in enumerate(pair_vec):
        result_vec[index] -= num_pairs
        left_insert_index, right_insert_index = integer_insertion_rules[index]
        result_vec[left_insert_index] += num_pairs
        result_vec[right_insert_index] += num_pairs
    
    return result_vec

def count_elements(pair_vec, indices):
    index_lookup = {v: k for k, v in indices.items()}
    counts = Counter()
    for index, num_pairs in enumerate(pair_vec):
        left_char, right_char = index_lookup[index]
        print(left_char, right_char, num_pairs)
        counts[left_char] += num_pairs
        counts[right_char] += num_pairs
    
    counts = Counter({k: round((v+0.5)/2, 0) for k,v in counts.items()})
    return counts

def subtract_least_from_most_common(counts):
    return counts.most_common()[0][1] - counts.most_common()[0][1]

if __name__ == '__main__':
    pair_vec, indices, integer_insertion_rules = read_input('input.txt')
    pair_vec = simulate_polymerization(pair_vec, integer_insertion_rules, steps=10)
    counts = count_elements(pair_vec, indices)
    result = subtract_least_from_most_common(counts)
    print(f"After 10 steps: {result}")
    pair_vec = simulate_polymerization(pair_vec, integer_insertion_rules, steps=30)
    counts = count_elements(pair_vec, indices)
    result = subtract_least_from_most_common(counts)
    print(f"After 40 steps: {result}")
