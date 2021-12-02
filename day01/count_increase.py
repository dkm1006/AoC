
INPUT_FILE = 'input.txt'

def read_sonar(sonar_report=INPUT_FILE):
    with open(sonar_report, 'r') as f:
        for reading in f:
            yield int(reading)

def count_increases(iterable):
    counter = 0
    previous_value = None
    for value in iterable:
        if previous_value is not None and value > previous_value:
            counter += 1
            print('Increased')
        else:
            print('Decreased')
        previous_value = value
    return counter

from itertools import islice

def sliding_window(iterable, window_size=2, fn=sum):
    iterator = iter(iterable)
    result = tuple(islice(iterator, window_size))
    if len(result) == window_size:
        yield fn(result)
    for element in iterator:
        result = result[1:] + (element,)
        yield fn(result)



def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result
