class test():
    def __init__(self):
        print("AAA")
    def __del__(self):
        print("BBB")
    def my(self):
        print("CCC")


obj=test()

obj.my()

del obj