def square(list1):
    list2 = []
    for value in list1:
        list2.append(value ** 2)
    return list2


print(square(range(1, 5)))

print(
    list(
        map(lambda x: x**2, range(1,5))
        )
)

print([x**2 for x in range(1,5)])