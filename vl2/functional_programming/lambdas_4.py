def calculate_string_list(value_list):
    result_list = []
    for value in value_list:
        result = calculate_string(value)
        result_list.append(result)
    return result_list


def calculate_string(value):
    if value < 10:
        return str(value) + " ist kleiner 10"
    elif value < 20:
        return str(value) + " ist zwischen 10 und 20"
    else:
        return str(value) + " ist größer 20"


def calculate_string_list_lambda(value_list):
    return list(
        map(
            lambda x: str(x) + " ist kleiner 10" if x < 10 else str(x) +
                                " ist zwischen 10 und 20" if x < 20 else str(x) +
                                 " ist größer 20",
            value_list
        )
    )


if __name__ == "__main__":
    integers = range(1, 30)
    result = calculate_string_list(integers)
    print(result)

    lambda_result = calculate_string_list_lambda(integers)
    print(lambda_result)
