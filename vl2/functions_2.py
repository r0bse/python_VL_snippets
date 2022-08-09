
def age_verification(age: int, age_to_be_allowed_to_drink: int) -> bool:
    return age >= age_to_be_allowed_to_drink


if __name__ == "__main__":
    print("With age 18 and threshold 21:  {0}".format(age_verification(18, 21)))
    print("With named parameters:         {0}".format(age_verification(age_to_be_allowed_to_drink=18, age=21)))
