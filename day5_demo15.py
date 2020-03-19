import multiprocessing
import time

def demo_worker():
    print('start worker')
    time.sleep(0.5)
    print('finish worker')

if __name__ == '__main__':
    p = multiprocessing.Process(target=demo_worker)
    print("before start:",p, p.is_alive())
    p.start()
    print("before start:", p, p.is_alive())
    p.terminate()
    print("after terminate:", p, p.is_alive())
    time.sleep(0.3)
    print("after terminate and sleep:", p, p.is_alive())
    p.join()
    print("after join():", p, p.is_alive())
