prefilled_set = {"any value", 1234, "is allowed"}
prefilled_set.add(1234)
for value in prefilled_set:
    print(value)

empty_set = set()
print(empty_set)

empty_set.add("string")
empty_set.add("string")
print(empty_set)

empty_set.remove("string")
print(empty_set)
