
def apply(func: object, *args, **kwargs):
    """

    :param func:  the function to trigger
    :param args: values without keyword
    :param kwargs: values with keyword
    :return:
    """

    return func(*args, **kwargs)

def exponential_growth(value = 0, exponent = 2):
    return value**exponent

if __name__ == "__main__":
    print(apply(exponential_growth, 3, 1)) #3
    print(apply(exponential_growth, value = 2, exponent=2)) #4
    print(apply(exponential_growth, exponent = 4)) #0
    print(apply(exponential_growth, 2, exponent = 8)) #256

