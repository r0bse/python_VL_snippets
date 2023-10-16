def add_params(arg1, arg2):
    return arg1 + arg2


lambda_add_params = lambda arg1, arg2: arg1 + arg2

if __name__ == "__main__":
    print(add_params("Hello", "World"))
    print(lambda_add_params("Hello", "World"))
