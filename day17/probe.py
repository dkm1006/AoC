import re
import numpy as np

def pos(v0, t):
    return x_pos(v0[0], t), y_pos(v0[1], t)

def x_pos(vx0, t):
    step = 1 if vx0 < 0 else -1
    x_array = np.array([0] + list(range(vx0, 0, step))).cumsum()
    return x_array[-1] if t > abs(vx0) else x_array[t]

def y_pos(vy0, t):
    return t*vy0 - np.arange(t).cumsum()[-1] if t else 0

def max_y_pos(vy0):
    return y_pos(vy0, abs(vy0))

def max_x_pos(vx0):
    return x_pos(vx0, abs(vx0))

def feasible_v0_area(target_area):
    min_x, max_x, min_y, max_y = target_area
    for vx0 in range(max_x+1):
        min_vx0 = vx0
        if max_x_pos(vx0) >= min_x:
            break
    return min_vx0, max_x, min_y, -min_y-1

def is_within_area(position, target_area):
    x, y = position
    min_x, max_x, min_y, max_y = target_area
    return (min_x <= x <= max_x) and (min_y <= y <= max_y)

def feasible_solutions(search_space, target_area, max_t_multiple=5):
    solution_set = set()
    min_vx0, max_vx0, min_vy0, max_vy0 = search_space
    for vx0 in range(min_vx0, max_vx0+1):
        for vy0 in range(min_vy0, max_vy0+1):
            v0 = (vx0, vy0)
            for t in range(max_t_multiple*max(v0)):
                x, y = pos(v0, t)
                if x > target_area[1] or y < target_area[2]:
                    break 
                elif is_within_area((x, y), target_area):
                    solution_set.add(v0)
                    break
                else:
                    continue
    
    return solution_set

def read_input(input_file):
    pattern = r"target area: x=(-?\d+)\.+(-?\d+), y=(-?\d+)\.+(-?\d+)"
    with open(input_file, 'r') as f:
        line = next(f).strip()
        match = re.search(pattern, line)
        return tuple(int(m) for m in match.groups())