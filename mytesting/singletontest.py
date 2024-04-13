from src.__utils.SingletonMeta import SingletonMeta


class single(metaclass=SingletonMeta):
    def __init__(self, msg):
        self.msg = msg

    def hi(self):
        print(self.msg)


if __name__ == "__main__":
    single(msg="H1 its 1").hi()
    single.remake(msg="Lmao").hi()
    single().hi()
