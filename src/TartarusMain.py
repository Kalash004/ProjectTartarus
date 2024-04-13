from src.program_layers.api_layer.controller.ApiLayerMain import ApiLayerMain
from src.program_layers.database_layer.controller.DatabaseController import DatabaseController

start = True


def wraper(func):
    def worker():
        global start

        def func_wrapper():
            global start
            try:
                func()
                start = False
                return
            except Exception as e:
                print(e)
                start = True

        while start:
            func_wrapper()

    return worker


@wraper
def main():
    """Program"""
    db_controller = DatabaseController()
    api_layer_controller = ApiLayerMain()
    api_layer_controller.start()


if __name__ == "__main__":
    """Main start point of the program"""
    main()
