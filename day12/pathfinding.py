from collections import deque, Counter

class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.is_small = id.islower()
        self.neighbours = set()
    
    def find_paths_to(self, target_id):
        valid_paths = []
        paths_to_try = deque()
        paths_to_try.append([self])
        while len(paths_to_try):
            path = paths_to_try.popleft()
            print(f"Init {path}")
            last_node = path[-1]
            while not last_node.id == target_id:
                already_visited_small = Counter(n for n in path if n.is_small)
                max_small = already_visited_small.most_common(1)[0][1]
                if max_small < 2:
                    already_visited_small = {self}
                neighbours = last_node.neighbours - set(already_visited_small)
                # print(f"Neighbours {neighbours}")
                if not neighbours:
                    print(f"Discard {path}")
                    break  # discard this path
                else:                    
                    last_node = neighbours.pop()
                    print(last_node, 'taken from', neighbours)
                    for other_neighbour in neighbours:
                        paths_to_try.append(path[:] + [other_neighbour])
                    
                    path.append(last_node)
            else:
                print(f"Save {path}")
                valid_paths.append(path)
        
        return valid_paths
    
    def get_next_neighbour(self):
        return next(iter(self.neighbours))
    
    def __repr__(self):
        return f"Node('{self.id}')"

    def __str__(self):
        return f"({self.id})"

class Path:
    def __init__(self):
        pass


def read_input(input_file):
    graph = {}
    with open(input_file, 'r') as f:
        for line in f:
            source, target = line.strip().split('-')
            graph = add_edge(graph, source, target)

    return graph

def add_edge(graph, source_id, target_id):
    source = graph.get(source_id, Node(source_id))
    target = graph.get(target_id, Node(target_id))
    source.neighbours.add(target)
    target.neighbours.add(source)
    graph[source_id] = source
    graph[target_id] = target
    return graph

if __name__ == '__main__':
    graph = read_input('input.txt')
    all_paths = graph['start'].find_paths_to('end')
    print(f"Total # paths: {len(all_paths)}")
    # for path in sorted(all_paths, key=len):
    #     print('-'.join(str(node) for node in path))
