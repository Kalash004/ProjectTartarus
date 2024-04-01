from src.utils.Singleton import singleton


@singleton
class my_single:
    def __init__(self, msg):
        self.msg = msg

    def hi(self):
        print(self.msg)


if __name__ == "__main__":
    my_single("s1 here").hi()