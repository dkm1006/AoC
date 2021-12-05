from collections import deque
import numpy as np

INPUT_FILE = 'input.txt'

class Bingo:
    def __init__(self, input_file):
        self.numbers_to_draw, self.boards = self.read_input(input_file)
        self.drawn_numbers = []
        self.winning_order = []

    def read_input(self, input_file):
        with open(input_file, 'r') as f:
            numbers_to_draw = deque(int(item) for item in next(f).split(','))
            boards = self.build_boards(f)
            return numbers_to_draw, boards

    def play(self):
        while len(self.winning_order) < len(self.boards):
            drawn_number = self.draw_number()
            print(f"Drawn number: {drawn_number}\n{'#'*40}")
            # TODO: Could pop the boards that have already won
            for board in self.boards:
                if not board.has_won:
                    board.mark_number(drawn_number)
                    print(f"{board}\n{'-'*20}")
                    if board.has_won:
                        self.winning_order.append(board.sum_unmarked * drawn_number)

    def let_squid_win(self):
        while len(self.numbers_to_draw):
            drawn_number = self.draw_number()
            print(f"Drawn number: {drawn_number}\n{'#'*40}")
            for board in self.boards:
                board.mark_number(drawn_number)
                print(f"{board}\n{'-'*20}")
                if board.has_won:
                    return board.sum_unmarked * drawn_number

    @property
    def last_drawn(self):
        return self.drawn_numbers[-1] if self.drawn_numbers else None
    
    def draw_number(self):
        drawn_number = self.numbers_to_draw.popleft()
        self.drawn_numbers.append(drawn_number)
        return drawn_number
    
    @staticmethod
    def build_boards(file_pointer):
        boards = []
        temp_list = []
        while True:
            try:
                values = next(file_pointer).split()
            except StopIteration:
                values = None
                break
            finally:
                if values:
                    numbers = [int(item) for item in values]
                    temp_list.append(numbers)
                elif temp_list:
                    boards.append(Board(temp_list))
                    temp_list = []

        return boards

class Board:
    def __init__(self, lines) -> None:
        self.matrix = np.array(lines)
        self.mask = np.ones_like(self.matrix)
        self.score = None
    
    def mark_number(self, number):
        self.mask[np.nonzero(self.matrix == number)] = 0

    @property
    def has_won(self):
        """Returns True if a row or column is all marked"""
        any_col_fully_marked = not self.mask.any(axis=0).all()
        any_row_fully_marked = not self.mask.any(axis=1).all() 
        return any_col_fully_marked or any_row_fully_marked

    @property
    def sum_unmarked(self):
        return (self.mask * self.matrix).sum()

    def __str__(self):
        lines = []
        for line, line_mask in zip(self.matrix, self.mask):
            line_str = ' '.join(
                f"{v:2}{' ' if is_remaining else '*'}"
                for v, is_remaining in zip(line, line_mask)
            )
            lines.append(line_str)

        return '\n'.join(lines)

if __name__ == '__main__':
    game = Bingo(INPUT_FILE)
    game.play()
    print(f"Winning score {game.winning_order[0]}")
    print(f"Losing score {game.winning_order[-1]}")
