from numpy import random

# example_amount = 10
# x = random.random(example_amount)
#
# example_amount = 10
# lower_bound = 3
# upper_bound = 10
# x = random.random_integers(lower_bound, upper_bound, example_amount)

if __name__ == "__main__":
    example_amount = 10
    lower_bound = 3
    upper_bound = 10
    x = random.random_integers(lower_bound, upper_bound, example_amount)
    print(x)

