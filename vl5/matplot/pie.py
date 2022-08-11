import matplotlib.pyplot as plt

slices = [7, 24, 12, 2, 9]
users = ["Batman", "Spider-Man", "Marvel Girl", "Stan Lee", "Donald Duck"]

plt.pie(slices, labels=users, colors=["c", "m","r", "b", "g" ])

if __name__ == '__main__':
    plt.show()