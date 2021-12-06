from collections import Counter

TIMER = 6

def initialize_clusters(input_file):
    fish_clusters = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(input_file, 'r') as f:
        # Count the number of fish with a certain timer value
        counts = Counter(int(timer) for timer in next(f).split(','))
        for cluster, count in counts.items():
            fish_clusters[cluster] = count

    return fish_clusters

def grow(input_file='input.txt', days_remaining=80):
    fish_clusters = initialize_clusters(input_file)
    # print(f"Initial state: {fish_clusters}")
    while days_remaining:
        newly_spawned = fish_clusters[0]
        fish_clusters = fish_clusters[1:] + [newly_spawned]
        fish_clusters[6] += newly_spawned
        days_remaining -= 1

    return fish_clusters


if __name__ == '__main__':
    days = 256
    result = grow(input_file='input.txt', days_remaining=days)
    print(f"After {days} days: {sum(result)} fish")