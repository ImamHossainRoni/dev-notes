class Singleton(object):
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance:
            raise Exception("Sorry! You can only instantiate one time of {0} class.".format(self.__class__.__name__))

        else:
            Singleton.__instance = self


obj1 = Singleton()
obj2 = Singleton()
