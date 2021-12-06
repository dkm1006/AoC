import numpy as np

MAP_SIZE = 1000

def read_input(input_file):
    result = []
    with open(input_file, 'r') as f:
        for line in f:
            p1, p2 = line.split(' -> ')
            x1, y1 = (int(v) for v in p1.split(','))
            x2, y2 = (int(v) for v in p2.split(','))
            result.append(((x1, y1), (x2, y2)))

    return result


class Line:
    def __init__(self, start, end, size=MAP_SIZE) -> None:
        self.start = start
        self.end = end
        self.matrix = np.zeros((size, size), dtype=np.int8)
        

class OceanMap:
    def __init__(self, size=MAP_SIZE) -> None:
        self.matrix = np.zeros((size, size), dtype=np.int8)

    def mark_line(self, start_point, end_point):
        x1, x2 = start_point[0], end_point[0]
        y1, y2 = start_point[1], end_point[1]
        x_sign = 1 if x1 <= x2 else -1
        y_sign = 1 if y1 <= y2 else -1
        x_coords = np.arange(x1, x2+x_sign, x_sign)
        y_coords = np.arange(y1, y2+y_sign, y_sign)
        self.matrix[y_coords, x_coords] += 1

    def mark_horizontal_or_vertical_line(self, start_point, end_point):
        x1, x2 = sorted((start_point[0], end_point[0]))
        y1, y2 = sorted((start_point[1], end_point[1]))
        self.matrix[y1:y2+1, x1:x2+1] += 1
    
    def overlapping_points(self, threshold=2):
        return self.matrix >= threshold

    def __str__(self):
        lines = []
        for line in self.matrix:
            lines.append(' '.join(f"{v:2}" if v else ' .' for v in line))
        
        return '\n'.join(lines)

def is_horizontal_or_vertical_line(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


if __name__ == '__main__':
    ocean_map = OceanMap(size=1000)
    lines = read_input('input.txt')
    for start, end in filter(is_horizontal_or_vertical_line, lines):
        ocean_map.mark_line(start, end)

    num_overlapping_points = ocean_map.overlapping_points(threshold=2).sum()
    print(f"# overlapping points (only h and v): {num_overlapping_points}")
    for start, end in filter(lambda l: not is_horizontal_or_vertical_line(l), lines):
        ocean_map.mark_line(start, end)
    
    num_overlapping_points = ocean_map.overlapping_points(threshold=2).sum()
    print(f"# overlapping points: {num_overlapping_points}")
        
    
