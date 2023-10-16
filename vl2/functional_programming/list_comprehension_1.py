def is_even(arg):
    return arg % 2 == 0


if __name__ == "__main__":
    new_list = []
    for value in range(10):
        potenz = value**2
        if is_even(potenz):
            new_list.append(potenz)

    print(new_list)
