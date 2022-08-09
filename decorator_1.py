from datetime import datetime


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper


@benchmark
def make_lst(val):
    lst = [i for i in range(val)]
    return lst


@benchmark
def make_set(val):
    s = {i for i in range(val)}
    return s


@benchmark
def make_dict(val):
    d = {i: i for i in range(val)}
    return d


lst = make_lst(100_000)
my_set = make_set(100_000)
me_dict = make_dict(100_000)
