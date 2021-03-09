
class A:
    def __new__(cls):
        print("A.__new__ llamado")
        this = super(A, cls).__new__(cls)
        print(this, hex(id(this)))
        return this

    def __init__(self):
        print("A.__init__ llamado")
        print(self, hex(id(self)))

if __name__ == '__main__':
    a = A()