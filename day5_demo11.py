import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name
    print(name, "start to work")
    time.sleep(2)
    print(name, "exiting")


def my_service():
    name = multiprocessing.current_process().name
    print(name, "start to work")
    time.sleep(4)
    print(name, "exiting")

if __name__ == '__main__':
    service = multiprocessing.Process(name="a_service", target=my_service)
    worker1 = multiprocessing.Process(name="worker1", target=worker)
    worker2 = multiprocessing.Process(target=worker) # 沒給名字就會預設Process-i

    service.start()
    worker1.start()
    worker2.start()
    print("main program terminate")