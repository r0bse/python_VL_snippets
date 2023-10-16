var = [val % 2 == 0 for val in range(10)]
print(var)

var = [val for val in range(10) if val > 5]
print(var)

l = range(5)
val = ['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l]
print(val)

list1 = [1,2,3]
list2 = ["a", "b", "c"]
result = [(x,y) for x in list1 for y in list2]
print(result)