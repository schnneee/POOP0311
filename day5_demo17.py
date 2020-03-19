import logging
import multiprocessing
import sys
import time

def worker():
    print("do some work")
    time.sleep(1)
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
