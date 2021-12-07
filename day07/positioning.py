import numpy as np

def read_input(input_file):
    with open(input_file, 'r') as f:
        return np.array([int(pos) for pos in next(f).split(',')])


def sol_part_1(positions):
    optimal_point = np.median(positions)
    diffs = np.abs(positions - optimal_point)
    return diffs.sum()


def sol_part_2(positions, cost_fn=np.cumsum):
    min_pos, max_pos = positions.min(), positions.max()
    costs = cost_fn(np.arange(max_pos - min_pos + 1))
    results = []
    for pos in range(min_pos, max_pos + 1):
        costs_for_pos = costs[np.abs(positions - pos)]
        results.append(costs_for_pos.sum())
    
    return np.array(results)

if __name__ == '__main__':
    positions = read_input('input.txt')
    print(f"Solution part 1: {sol_part_1(positions)}")
    print(f"Solution part 2: {sol_part_2(positions).min()}")