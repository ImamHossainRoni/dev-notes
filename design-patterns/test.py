class Singleton(object):
    __instance = None

    def __init__(self):
        if Singleton.__instance:
            raise Exception("This is a Singleton class")

        else:
            Singleton.__instance = self


obj = Singleton()
obj2 = Singleton()
