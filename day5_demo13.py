import multiprocessing, time


def daemon():
    print('start daemon')
    for i in range(5):
        print(".", i)
        time.sleep(1)
    print('end daemon')


def daemon2():
    print('start daemon2')
    for i in range(5):
        print(".", i)
        time.sleep(2)
    print('end daemon2')


if __name__ == '__main__':
    d1 = multiprocessing.Process(target=daemon)
    d2 = multiprocessing.Process(target=daemon2)
    d1.daemon = True
    d2.daemon = True
    d1.start()
    d2.start()
    d1.join()
    d2.join() # = await
    print('now program terminated')
