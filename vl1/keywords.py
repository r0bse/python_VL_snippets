import keyword

if __name__ == "__main__":
    print(keyword.kwlist)

if (True):
    print(True)
elif (False):
    print(False)
else:
    print("else")

import keyword
from keyword import kwlist

from keyword import kwlist as alias_for_kwlist

print(alias_for_kwlist)

version = None

true = True
false = False

if (true and true):
    print("true and true")

if (true or false):
    print("true or false")

if (true and not false):
    print("true and not false")

# ['', '', '', '', '', 'assert', 'async', 'await', '', '', '', '', 'del', '', '', '', '', '', '', '', '', '', 'in', 'is', 'lambda', 'nonlocal', '', '', '', '', '', '', '', 'with', 'yield']

running_loop = True
while (running_loop):
    for value in list(range(10)):
        print(value)
        if (running_loop):
            running_loop = False
            continue
        else:
            break


class Example:
    def return_foo(self):
        return "foo"


try:
    raise Exception()
except Exception:
    print("caught exception")
finally:
    print("finally is always executed")

def declare_global():
    global x
    x = "hello global"


declare_global()
print(x)

for x in [0, 1, 2]:
    pass

for value in [1,2,3,4,5]:
    print(value)
else:
    print("done")

x = 10
i = 0
while(i<x):
    print(i)
    i=i+1
else:
    print("done, i is now ", i)

# forrest= True
# while(forrest):
#     # Run Forrest, run!
#     pass

print("started infinite loop, insert 'stop' to break loop and skip to skip lengtht calculation")
while True:
    s = input("insert text:")
    if s == "stop":
        break
    elif s == "skip":
        continue
    else:
        print("The length of inserted text is:", len(s))

def declare_nonlocal():
    x = "foo"
    def nested_declare_nonlocal():
        nonlocal x
        x = "hello nonlocal"
    nested_declare_nonlocal()
    return x

print(declare_nonlocal())


def default_declaration():
    x = "bar"
    def nested_default_declaration():
        x = "hello default"
    nested_default_declaration()
    return x

print(default_declaration())


x = "hello"

assert x == "hello"
# assert x == "this is false"

x = ["apple", "banana", "cherry"]
y = x
print(x is y)

x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]

print(x is y)

x = lambda a : a + 10
print(x(5))

with open("example.txt", "w") as file:
    file.write("Hello World!")

f = open("example.txt", "w")
try:
    f.write("hello world")
finally:
    f.close()


def simple_generator_fun():
    """
    A Simple Python program to demonstrate working
    of yield
    A generator function that yields 1 for the first time,
    2 second time and 3 third time
    """
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simple_generator_fun():
    print(value)