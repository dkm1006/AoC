from bisect import insort
OPEN_CHARS = '([{<'
CLOSING_CHARS = ')]}>'
OPEN_CLOSE_PAIRS = {o:c for o, c in zip(OPEN_CHARS, CLOSING_CHARS)}
CLOSING_PAIRS = {c:o for o, c in OPEN_CLOSE_PAIRS.items()}
CORRUPTED_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
AUTOCOMPLETE_SCORES = {')': 1, ']': 2, '}': 3, '>': 4}

def read_input(input_file):
    with open(input_file, 'r') as f:
        return f.read().split('\n')

def process_lines(lines):
    corrupted_score = 0
    autocomplete_scores = []
    for line in lines:
        try:
            open_chunks = find_open_chunks(line)
        except WrongClosingError as e:
            print(e.message)
            corrupted_score += CORRUPTED_SCORES[e.illegal]
        else:
            line_score = score_open_chunks(open_chunks)
            print(len(open_chunks), f"open chunks, total score {line_score}.")
            insort(autocomplete_scores, line_score)
    
    mid_pos = len(autocomplete_scores) // 2
    autocomplete_score = autocomplete_scores[mid_pos]
    return corrupted_score, autocomplete_score

def find_open_chunks(line):
    open_chunks = []
    for c in line:
        if c in OPEN_CLOSE_PAIRS:
            open_chunks.append(c)
        else:
            last_opened_chunk = open_chunks.pop()
            expected_closing = OPEN_CLOSE_PAIRS[last_opened_chunk]
            if c != expected_closing:
                raise WrongClosingError(expected=expected_closing, illegal=c)
    else:
        return open_chunks

def score_open_chunks(open_chunks):
    score = 0
    for c in reversed(open_chunks):
        score *= 5
        score += AUTOCOMPLETE_SCORES[OPEN_CLOSE_PAIRS[c]]
    return score

class WrongClosingError(Exception):
    """
    Raised when an illegal closing character is encountered.
    Attributes:
        expected  -- expected closing character
        illegal -- found closing character
    """
    def __init__(self, expected, illegal):
        self.expected = expected
        self.illegal = illegal
        self.message = f"Expected {expected}, but found {illegal} instead."

if __name__ == '__main__':
    lines = read_input('input.txt')
    corrupted_score, autocomplete_score = process_lines(lines)
    print(f"Total corrupted score: {corrupted_score}")
    print(f"Total autocomplete score: {autocomplete_score}")