x = None
if bool(x): # equivalent to "if x"
    print("can't be reached")
else:
    x = "initialized in else branch"

if bool(x):
    print(x)
else:
    raise Exception()