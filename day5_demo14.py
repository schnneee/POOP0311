import multiprocessing, time


def daemon():
    print('Daemon[%s]start:' % (multiprocessing.current_process().name))
    time.sleep(2)
    print('Daemon[%s]exit:' % (multiprocessing.current_process().name))


def non_daemon():
    print('Non Daemon[%s]start:' % (multiprocessing.current_process().name))
    time.sleep(2)
    print('Non Daemon[%s]exit:' % (multiprocessing.current_process().name))


if __name__ == '__main__':
    d1 = multiprocessing.Process(name='Daemon1', target=daemon)
    d1.daemon = True
    n1 = multiprocessing.Process(name='NonDaemon1', target=non_daemon)
    n1.daemon = False
    print('[1]before start, d1 is_alive?', d1.is_alive())
    print('[1]before start, n1 is_alive?', n1.is_alive())

    d1.start()
    n1.start()
    print('[2]after start, d1 is_alive?', d1.is_alive())
    print('[2]after start, n1 is_alive?', n1.is_alive())

    d1.join(1) # 相當於等一秒?
    print('[3]after d1 join(1), d1 is_alive?', d1.is_alive())
    print('[3]after d1 join(1), n1 is_alive?', n1.is_alive())
    time.sleep(1)
    n1.join() # 不給就是等到死
    print('[4]after n1 join(1), d1 is_alive?', d1.is_alive())
    print('[4]after n1 join(1), n1 is_alive?', n1.is_alive())

    # d1.join()
    d1.terminate()
    n1.terminate()
    print('[5]after terminate, d1 is_alive?', d1.is_alive())
    print('[5]after terminate, n1 is_alive?', n1.is_alive())
    time.sleep(1)
    print('[6]after terminate and wait 1 sec, d1 is_alive?', d1.is_alive())
    print('[6]after terminate and wait 1 sec, n1 is_alive?', n1.is_alive())
