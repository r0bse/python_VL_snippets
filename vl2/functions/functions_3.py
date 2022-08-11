
def age_verification(age: int = 0, age_to_be_allowed_to_drink: int = 18) -> bool:
    """
    verification that given age is allowed to drink
    :param age: defaults t 0
    :param age_to_be_allowed_to_drink: defaults to 18
    :return: true/false
    """
    return age >= age_to_be_allowed_to_drink


if __name__ == "__main__":
    age_verification()
