def maximum_of_two(arg1, arg2):
    if arg1 > arg2:
        return arg1
    else:
        return arg2


lambda_maximum = lambda arg1, arg2: arg1 if arg1 > arg2 else arg2

if __name__ == "__main__":
    print(maximum_of_two(1337, 42))
    print(lambda_maximum(1337, 42))
