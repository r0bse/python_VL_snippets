import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.barh(
        ["e", "*", "§", "d", "A", ";", "?", "$", "6", "j"],
        [12, 23, 28, 34, 36, 56, 78, 89, 90, 99],
        color="g")

    plt.show()