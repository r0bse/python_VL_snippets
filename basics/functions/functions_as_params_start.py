
def apply(func, values: list):
    """
    Applies function 'func' to each given element in list
    and puts result in a returned list
    ----------
    func : the function to be called
    list: all elements will be used to call given function
    -------
    result: resulting list
    """

    resultList = [] # neue Ergebnisliste initialisieren
    for i in range(len(values)): # für jedes element in übergebener liste

        # hole das aktuelle Objekt aus der übergebenen Liste
        value = values[i]
        # führe die übergebene Funktion mit dem Objekt aus
        # und weise das Ergebnis des resultierenden Funktionsaufruf einer variable zu
        return_value = func(value)
        # füge die Variable die auf die Funktion weist einer Liste hinzu
        resultList.append(return_value)

    return resultList

def square_root(number):
    return number**2

if __name__ == "__main__":

    print(apply(abs, [1, -2, -5, 6.2])) # [1, 2, 5, 6.2]
    print(apply(int, [1, -2, -5, 6.2]))  # [1, -2, -5, 6]
    print(apply(square_root, [1, -2, -5, 6.2]))  # [1, 4, 25, 38.440000000000005]

