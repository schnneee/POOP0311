import multiprocessing


def worker():
    print("worker do some work...")
    return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        print('now execute part %d' % i)
        p = multiprocessing.Process(target=worker) # async
        jobs.append(p)
        p.start()

    print("result=", jobs)
