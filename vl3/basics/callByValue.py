
int = 10
print("in int, beginn: ", int)

def call_by_value(int, int_in_fkt = 0):
    """how call by value works in python"""
    print("in int, davor: ", int)
    print("in int_in_fkt, davor: ", int_in_fkt)
    int_in_fkt = int_in_fkt + int_in_fkt
    int=int_in_fkt
    print("in int, danach: ", int)
    print("in int_in_fkt, danach: ", int_in_fkt)

call_by_value(int, 999)

print("in int, ende: ", int)
