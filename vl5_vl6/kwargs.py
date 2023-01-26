def myfunc2(**kwargs):
    for k, v in (kwargs.items()):
        print(k,v, sep="->", end=" ")
    if kwargs:
        print()

if __name__ == "__main__":
    myfunc2(a=1, b=2, c=3, d="something, something")