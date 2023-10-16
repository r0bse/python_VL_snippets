no_param_lambda = lambda: 2 * 2


def double(arg):
    return arg * 2


lambda_double = lambda arg: 2 * arg

if __name__ == "__main__":
    print(double(10))
    print(lambda_double(2))
    print(double(lambda_double(2)))
    print(double(double(2)))
