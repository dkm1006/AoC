import time

def timing(func):
    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print(f'{func.__name__} took: {te-ts:2.5f} sec')
        return result

    return timed