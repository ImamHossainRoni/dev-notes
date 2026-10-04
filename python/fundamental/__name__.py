print(__name__)
def fun1():
    print("from fun 1")
def fun2():
    print("from fun 2")

def main():
    fun1()
    fun2()
    print("from main function",__name__)
if __name__ == '__main__':
    main()