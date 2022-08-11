
def apply(func, *args):
    """
    Applies function 'func' to each given element
    ----------
    func : the function to be called
    *args: all given values will be applied
    -------
    result: resulting list
    """

    resultList = [] # neue liste initialisieren
    for i in range(len(args)): # für jedes element in übergebener liste

        # hole das aktuelle Objekt aus dem übergebenen Tuple
        arg = args[i]
        # führe die übergebene Funktion mit dem Objekt aus
        # und weise das Ergebnis des resultierenden Funktionsaufruf einer variable zu
        function = func(arg)
        # füge die Variable die auf die Funktion weist einer Liste hinzu
        resultList.append(function) # füge

    return resultList

def square_root(number):
    return number**2

if __name__ == "__main__":

    print(apply(abs, 1, -2, -5, 6.2)) # [1, 2, 5, 6.2]
    print(apply(int, 1, -2, -5, 6.2))  # [1, -2, -5, 6]
    print(apply(square_root, 1, -2, -5, 6.2))  # [1, 4, 25, 38.440000000000005]

