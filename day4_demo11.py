import functools
import time


def timer(func):
    def wrapper_timer(*args, **kwargs):
        startTime = time.perf_counter()
        value = func(*args, **kwargs)
        endTime = time.perf_counter()
        runTime = endTime - startTime
        print("this {!r} spend {:.4f}".format(func.__name__, runTime))
        return value

    return wrapper_timer


@timer
def spend_time_to_calculate(num_times):
    total = 0
    for _ in range(num_times):
        total = sum([i ** 2 for i in range(10000)])
    return total


repeats = [1, 5, 10, 50, 100, 500, 1000]
for repeat in repeats:
    print("[%d]result = %d" % (repeat, spend_time_to_calculate(repeat)))