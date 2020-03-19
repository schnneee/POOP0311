import multiprocessing, sys, time

def exit_error():
    sys.exit(5)

def exit_ok():
    return

def return_value():
    return 1

def raiseAError():
    raise RuntimeError("There was an error!")

def terminated():
    time.sleep(3)

if __name__ == '__main__':
    jobs = []
    for fun in [exit_error, exit_ok, return_value, terminated]:
        print('start process for:', fun.__name__)
        j = multiprocessing.Process(target=fun, name=fun.__name__)
        jobs.append(j)
        j.start()
    jobs[-1].terminate()
    for j in jobs:
        j.join()
        print("%s exit code=%s"%(j.name, j.exitcode))

    for f in [raiseAError]:
        print('start a process for:', f.__name__)
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()