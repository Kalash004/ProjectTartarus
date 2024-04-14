from src.program_layers.api_layer.controller.ApiLayerMain import ApiLayerMain
from src.program_layers.database_layer.controller.DatabaseController import DatabaseController

start = True


def program_exception_restart(func):
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


@program_exception_restart
def main():
    """Program"""
    # start the database
    db_controller = DatabaseController()
    # start the server
    api_layer_controller = ApiLayerMain()
    api_layer_controller.start()


if __name__ == "__main__":
    """Main start point of the program"""
    main()
