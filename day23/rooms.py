from dataclasses import dataclass

EMPTY_HALLWAY = (0,) * 11
COSTS = {a:10**a-1 for a in (1, 2, 3, 4)}
# COSTS = {a:10**i for i,a in enumerate('ABCD')}

@dataclass
class State:
    rooms: tuple
    hallway: tuple=EMPTY_HALLWAY
    cost: int=0

    def reachable_states(self):
        best_result = None  # goal state w/ cost to get there
        for index, amphipod in enumerate(self.hallway):
            if amphipod:
                # move into the destination
                pass
        
        for index, amphipod in enumerate(self.rooms):
            if self.can_move_out(amphipod, index):
                # move out into the hallway
                pass
        
        return best_result

    def is_goal_state(self):
        last_amphipod = 0
        for amphipod in self.hallway + self.rooms:
            if amphipod < last_amphipod:
                return False
            last_amphipod = amphipod
        else:
            return True

    def __hash__(self) -> int:
        return sum(attr.__hash__() for attr in (self.rooms, self.hallway, self.cost))
    

start_state = State(rooms=(2,1,3,4,2,3,4,1))
goal_state = State(rooms=tuple(sorted(start_state.rooms)))
