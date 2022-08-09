
prefilled_tuple=("any value", 1234, "is allowed")

for value in prefilled_tuple:
    print(value)

#

print(prefilled_tuple.count(1234)) # Output 1
print(prefilled_tuple.index("is allowed")) # Output 2