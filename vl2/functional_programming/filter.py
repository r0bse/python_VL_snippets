def is_string(arg):
    return isinstance(arg, str)


lst = ['c', "string", 12, "anderer string", 5.34]

new_list = []
for value in lst:
    if is_string(value):
        new_list.append(value)
print(new_list)

print(
    list(
        filter(
            lambda x: isinstance(x, str), lst
        )
    )
)

print(
    [x for x in lst if isinstance(x, str)]
)