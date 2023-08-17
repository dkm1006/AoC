from itertools import accumulate, cycle
from dataclasses import dataclass, field

WINNING_SCORE = 1000

@dataclass
class Game:
    player_positions: list[int] = field(default_factory=list)
    player_scores: list[int] = field(default_factory=list)
    die: list[int] = field(default_factory=lambda:cycle(range(1, 101)))
    total_num_throws: int = 0

    def sum_next_throws(self, num_throws=3):
        total = 0
        for i in range(num_throws):
            total += next(self.die)
            self.total_num_throws += 1
        return total
    
    def advance_player(self, player_index, num_throws=3):
        thrown_total = self.sum_next_throws(num_throws=num_throws)
        current_position = self.player_positions[player_index]
        new_position = (current_position - 1 + thrown_total) % 10 + 1
        self.player_positions[player_index] = new_position
        self.player_scores[player_index] += new_position
        return self.player_scores[player_index]
    
    def play(self):
        player_iter = cycle(range(len(self.player_positions)))
        current_score = 0
        while current_score < WINNING_SCORE:
            player_index = next(player_iter)
            current_score = self.advance_player(player_index)
            print(current_score)
        else:
            num_throws = self.total_num_throws
            print(f"Player {player_index} has won after {num_throws} throws.")
            print(f"Losing player score: {self.player_scores[next(player_iter)]}")
    
    @property
    def summary(self):
        return self.total_num_throws * min(self.player_scores)

