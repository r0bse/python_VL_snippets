
class Callable:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("Class Callable called with ", args, kwargs)

def apply(func: object, *args, **kwargs):
    """

    :param func:  the function to trigger
    :param args: values without keyword
    :param kwargs: values with keyword
    :return:
    """

    return func(*args, **kwargs)


if __name__ == "__main__":
    apply(Callable(), 3, 1)
    apply(Callable(), value = 2, exponent=2)
    apply(Callable(), exponent = 4)
    apply(Callable(), 2, exponent = 8)

