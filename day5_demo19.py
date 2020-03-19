import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("start a thread:" + self.name)
        print_time(self.name, self.counter, 2)
        # for i in range(5):
        #     time.sleep(1)
        #     print("[%s]process:%d" % (self.name, self.counter))
        print("finish a thread:" + self.name)


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            currentThread.exit()
        time.sleep(delay)
        print("%s,%s" % (threadName, time.ctime(time.time())))
        counter -= 1


t1 = myThread(1, "Thread-1", 1)
t2 = myThread(2, "Thread-2", 2)

t1.start()
t2.start()
t1.join()
t2.join()
print("Quit Main Thread")
