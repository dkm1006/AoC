from itertools import islice
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
            # print('Increased')
        else:
            # print('Decreased')
            pass
        previous_value = value
    return counter

def sliding_window(iterable, window_size=3, fn=sum):
    iterator = iter(iterable)
    result = tuple(islice(iterator, window_size))
    if len(result) == window_size:
        yield fn(result)
    for element in iterator:
        result = result[1:] + (element,)
        yield fn(result)
