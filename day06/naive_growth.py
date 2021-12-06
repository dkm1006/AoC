TIMER = 6

class Fish:
    def __init__(self, timer=TIMER+2):
        self.timer = timer

    def tick(self):
        has_spawned = self.timer == 0
        self.timer = TIMER if has_spawned else self.timer - 1
        return has_spawned
    
    def __str__(self):
        return str(self.timer)

    def __repr__(self):
        return f"{self.__class__.__name__}(timer={self.timer})"

def initialize_school(input_file):
    with open(input_file, 'r') as f:
        return [Fish(int(timer)) for timer in next(f).split(',')]

def grow(initial_school, days_remaining=80):
    # counter = 0
    school = initial_school[:]
    # print(f"Initial state: {','.join([str(fish) for fish in school])}")
    while days_remaining:
        newly_spawned = []
        for fish in school:
            if fish.tick():
                newly_spawned.append(Fish())
            
        school.extend(newly_spawned)
        days_remaining -= 1
        # counter += 1
        # print(f"After {counter:2} days: {','.join([str(fish) for fish in school])}")

    return school

if __name__ == '__main__':
    days = 80
    initial_school=initialize_school('input.txt')
    result = grow(initial_school, days_remaining=days)
    print(f"After {days} days: {len(result)} fish")