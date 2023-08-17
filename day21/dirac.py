from itertools import accumulate, combinations, cycle, product, repeat
from dataclasses import dataclass, field
from collections import Counter
from functools import lru_cache

WINNING_SCORE = 21


def setup_game(player_positions):
    player_scores = [0 for player in player_positions]
    universe = tuple(
        (pos, score) for pos, score
        in zip(player_positions, player_scores)
    )
    return [universe]

def play_round(universes_in_play):
    won_universes = Counter()
    while universes_in_play:
        universe = universes_in_play.pop()
        pos0, score0 = universe[0]
        for new_pos0 in possible_end_positions(pos0):
            final_score0 = new_pos0 + score0
            if final_score0 >= WINNING_SCORE:
                won_universes[0] += 1
            else:
                pos1, score1 = universe[1]
                for new_pos1 in possible_end_positions(pos1):
                    final_score1 = new_pos1 + score1
                    if final_score1 >= WINNING_SCORE:
                        won_universes[1] += 1
                
                    universes_in_play.append(((new_pos0, final_score0), (new_pos1, final_score1)))
                    print(len(universes_in_play), won_universes)

@lru_cache
def possible_end_positions(current_position):
    move_sequences = product(*repeat((1, 2, 3), 3))
    cumulated_moves = map(sum, move_sequences)
    return (
        calc_new_position(current_position, move) for move in cumulated_moves
    )

def calc_new_position(current_position, move, modulo=10):
    return (current_position + move - 1) % modulo + 1