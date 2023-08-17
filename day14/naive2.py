def replace(sequence, memo=insertion_rules):
    if sequence in memo:
        result = memo.get(sequence)
    elif len(sequence) == 1:
        result = sequence
        memo[sequence] = result
    else:
        midpoint = len(sequence) // 2
        first = sequence[:midpoint]
        mid = sequence[midpoint-1:midpoint+1]
        last = sequence[midpoint:]
        result = replace(first, memo) + replace(mid, memo)[1] + replace(last, memo)
        memo[sequence] = result
    
    return result

def simulate_polymerization(polymer, insertion_rules, steps=10):
    for step in range(steps):
        polymer = replace(polymer, memo=insertion_rules)
    
    return polymer

