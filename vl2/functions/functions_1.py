
def age_verification(age, age_to_be_allowed_to_drink):
    return age >= age_to_be_allowed_to_drink


if __name__ == "__main__":
    print("No parameter resolved to:      {0}".format(age_verification()))
    print("With age 18 resolves to:       {0}".format(age_verification(18)))
    print("With age 18 and threshold 21:  {0}".format(age_verification(18, 21)))
    print("With named parameters:         {0}".format(age_verification(age_to_be_allowed_to_drink=18, age=21)))
