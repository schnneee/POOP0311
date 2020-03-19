import multiprocessing
import time


def daemon():
    print('start daemon')
    for i in range(6):
        time.sleep(1)
        print("daemon.")
    print('end daemon')


def non_daemon():
    print('start process',multiprocessing.current_process().name)
    for i in range(6):
        time.sleep(1)
        print("doing..",multiprocessing.current_process().name)
    print('end process',multiprocessing.current_process().name)


if __name__ == '__main__':
    daemon1 = multiprocessing.Process(name='daemon', target=daemon)
    daemon1.daemon = True # 會和 main thread一同終止
    process = multiprocessing.Process(name='process', target=non_daemon)
    process.daemon = False
    process2 = multiprocessing.Process(name='process2', target=non_daemon)
    process2.daemon = False

    daemon1.start()
    time.sleep(2)
    process.start()
    process2.start()
