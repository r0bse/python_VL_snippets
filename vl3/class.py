
class BspClass:

    def __init__(self, x=1, y=89):
        self.x = x
        self.y = y


    def do_something(self):
        print("do_something()")
        self.x += 45
        return self.x

bsp = BspClass()

print("bsp.x = ", bsp.x)
print("bsp.x = ", bsp.y)

bsp.do_something()

print("bsp.x = ", bsp.x)
print("bsp.x = ", bsp.y)
