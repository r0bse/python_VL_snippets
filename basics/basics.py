variable1 = 1
variable2 = "ein String"

integer = 1234
long = 999999999999999999999999999999
string = "text"
float = 3.14

print(integer, long, string, float)

print(type(integer))
print(type(long))
print(type(string))
print(type(float))

print("please enter a digit")
x = int(input())
if x > 4:
    print(x, "is bigger than 4")
elif x < 4:
    print(x, "is smaller than 4")
else:
    print(x, "equals than 4")


def age_verification(age, ageToBeAllowedToDrink):
    """"
    verificates the age to be allowed to drink
    """
    if (age >= ageToBeAllowedToDrink):
        drinkAllowed = True

    return drinkAllowed


def do_something(i, v):
    """
    if i is bigger or equals v, return True
    """
    a = False
    if (i >= v):
        a = True
    return a


do_something(1, 2)


def age_verification(age:int, ageToBeAllowedToDrink:int) -> bool:
    """
    verificates the age to be allowed to drink
    """
    return age >= ageToBeAllowedToDrink

age_verification(19,18) #True
age_verification(ageToBeAllowedToDrink=18, age=7) # false
age_verification(ageToBeAllowedToDrink=18) # False
age_verification() # True


for value in range(10):
    print(value)

for value in range(3, 10, 2):
    print(value)  # 3, 5, 7, 9
