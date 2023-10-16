from functools import reduce


def add(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum


print(add(range(42)))

print(
    reduce(
        lambda x,y: x+y, range(42)
    )
)
