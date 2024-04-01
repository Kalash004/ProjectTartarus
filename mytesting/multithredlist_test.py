import threading


class One:
    def __init__(self, name):
        self.name = name

    def print_it(self, msg):
        print(f"{self.name} - {msg}")


class Multiple:
    @staticmethod
    def send(msg, reciever):
        for i in range(0, 10):
            reciever.print_it(f"{i}:{msg}")


if __name__ == "__main__":
    m1 = Multiple()
    m2 = Multiple()
    o = One("RRR")
    t1 = threading.Thread(target=m1.send, args=("t1", o))
    t2 = threading.Thread(target=m2.send, args=("t2", o))
    t1.start()
    t2.start()
