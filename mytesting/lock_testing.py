import threading
from time import sleep

if __name__ == "__main__":
    counter = 0
    lock = threading.Lock()


    def execute(msg: str):
        global counter
        print(f"now waiting for {msg}")
        counter = counter + 1
        sleep(1)


    def target(msg):
        global lock
        lock.acquire()
        for i in range(0, 10):
            execute(msg)
        lock.release()


    t1 = threading.Thread(target=target, args=("t1",))
    t2 = threading.Thread(target=target, args=("t2",))
    t3 = threading.Thread(target=target, args=("t3",))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print(counter)
