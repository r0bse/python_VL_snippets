
# When Immutable objects such as whole numbers, strings,
# etc are passed as arguments to the function call,
# it can be considered as Call by Value.
#
# This is because when the values are modified within the function,
# then the changes do not get reflected outside the function.

def call_by_value(a):
    print("\t Value received in 'a' =", a)
    a+=2
    print("\t Value of 'a' changes in function to :",a)

if __name__ == "__main__":
    num=13
    print("Initial number: ", num)
    call_by_value(num)
    print("Value of number after function = ", num)