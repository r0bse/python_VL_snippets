
def drink_age_verification(age = 0, age_to_be_allowed_to_drink = 18):
    return age >= age_to_be_allowed_to_drink

def multiple_returns(age = 0, age_to_be_allowed_to_drink = 18):
    allowed_to_drink = age >= age_to_be_allowed_to_drink
    if(allowed_to_drink):
        return allowed_to_drink, 0
    else:
        missing_years = age_to_be_allowed_to_drink - age
        return allowed_to_drink, missing_years

if __name__ == "__main__":

    # drinking_allowed = drink_age_verification()
    # print("No Params resolves to: {0}".format(drinking_allowed))
    #
    # age = 18
    # drinking_allowed = drink_age_verification(age)
    # print("With age Param '{0}' resolves to: {1}".format(age, drinking_allowed))
    #
    # age = 20
    # treshold = 21
    # drinking_allowed = drink_age_verification(age, treshold)
    # print("With both params resolves to: {0}".format(drinking_allowed))
    #
    # age = 37
    # treshold = 21
    # drinking_allowed = drink_age_verification(age_to_be_allowed_to_drink=treshold, age= age)
    # print("With both params named and switched resolves to: {0}".format(drinking_allowed))

    age = 15
    treshold = 21
    allowed, difference = multiple_returns(age, treshold)
    print("With the age {0}, you are missing {1} years to be allowed to drink".format(age, difference))


