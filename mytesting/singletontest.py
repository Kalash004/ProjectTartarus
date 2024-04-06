from src.utils.SingletonMeta import SingletonMeta


class single(metaclass=SingletonMeta):
    def __init__(self, msg):
        self.msg = msg

    def hi(self):
        print(self.msg)


if __name__ == "__main__":
    s1 = single(msg="H1 its 1")
    s1.hi()
    s2 = single(msg="Lmao")  # type:ignore
    s2.hi()
    s1.hi()
