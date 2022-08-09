print("id of an integer =", id(5))

set_a = {1, "a", 3.4}
print("id of set =", id(set))

set_b = set_a
print("id of copied set_b =", id(set_b))

class Foo:
    ...
print("id of a class =", id(Foo()))
