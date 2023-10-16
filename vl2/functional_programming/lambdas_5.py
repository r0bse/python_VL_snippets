def sequential_processing_a_list(value):
    if value > 5:
        return 1
    else:
        return 0


if __name__ == "__main__":
    liste = range(1, 10)
    print( list(map(sequential_processing_a_list, liste) ))