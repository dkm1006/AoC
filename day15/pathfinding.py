from queue import PriorityQueue
from collections import deque
from dataclasses import dataclass
import numpy as np

@dataclass
class Node:
    coords: tuple
    densitymap: np.array
    predecessor: 'Node' = None
    cost: int = 99999999999999
    f_score: int = 99999999999999
    
    @property
    def density(self):
        return self.densitymap[self.coords]
    
    def __str__(self):
        return f"Node(coords={self.coords}, density={self.density})"

class Pathfinder:
    def __init__(self, costmap, start=None, end=None):
        self.costmap = costmap
        start = (0, 0) if start is None else start
        end = (costmap.shape[0]-1, costmap.shape[1]-1) if end is None else end
        self.start = Node(start, costmap, cost=0)
        self.end = Node(end, costmap)

    @classmethod
    def from_file(cls, input_file):
        costmap = np.genfromtxt(input_file, delimiter=1, dtype=int)
        return cls(costmap)

    def find_lowest_total_risk(self):
        risk_estimator = risk_estimator_factory(self.end)
        optimal_path = find_optimal_path(self.start, self.end, risk_estimator)
        total_risk = sum(node.density for node in optimal_path)
        return total_risk
    
    def find_optimal_path(self):
        fringe = PriorityQueue()
        fringe.put((self.start.cost, self.start))
        while not fringe.empty():
            current_node = fringe.get()
            if current_node.coords == self.end.coords:
                break

            for neighbour in self.get_neighbours(current_node):
                tentative_score = current_node.cost + neighbour.density
                if tentative_score < neighbour.cost:
                    neighbour.cost = tentative_score
                    neighbour.predecessor = current_node
                    neighbour.f_score = tentative_score + risk_estimator(neighbour)
                    if neighbour not in fringe:
                        fringe.put(neighbour)

        return reconstruct_path(current_node)

    def get_neighbours(self, node):
        pass



def read_input(input_file):
    return np.genfromtxt(input_file, delimiter=1, dtype=int)

def find_lowest_total_risk(densitymap, start=(0, 0), end=None):
    if end is None:  # if no end is given, take bottom right corner
        end = densitymap.shape[0], densitymap.shape[1]

    risk_estimator = risk_estimator_factory(end)
    optimal_path = find_optimal_path(start, end, risk_estimator)
    total_risk = sum(node.density for node in optimal_path)
    return total_risk

def reconstruct_path(current_node):
    path = deque([current_node])
    while current_node.predecessor:
        current_node = current_node.predecessor
        path.appendleft(current_node)
    return path

def find_optimal_path(start, end, cost_estimator):
    fringe = PriorityQueue()
    current_node = start
    start.cost = 0

    
    return reconstruct_path(last_node)


def risk_estimator_factory(end,
                           distance_measure='manhattan',
                           cost_attribute='density',
                           default_cost=0):
    """
    Factory function for cost estimators for A* algorithm

    Interface: 
    end - Target node 
    distance_measure - one of 'manhattan' 
    cost_attribute - node attribute that contains the cost for that node 
    default_cost - default value for cost_attribute 
    """
    distance_functions = {
        'manhattan': manhattan_distance
    }
    distance_fn = distance_functions[distance_measure]
    def risk_estimator(node):
        # Adds the distance to end + the node's cost
        distance = distance_fn(end.coords, node.coords)
        return getattr(node, cost_attribute, default_cost) + distance
    
    return risk_estimator

def manhattan_distance(a, b):
    return sum(abs(m-c) for m, c in zip(a, b))

if __name__ == '__main__':
    densitymap = read_input('input.txt')