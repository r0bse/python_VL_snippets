from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code der ausgeführt werden soll bevor die dekorierte Funktion aufgerufen wird
        if (1 == 1):
            # 2. Aufruf der dekorierten Funktoin mit return des Ergebnisses sofern es benötigt wird
            return func(*args, **kwargs)
        # 3. der Code der ausgeführt werden soll ANSTATT die dekorierte Funktion aufzurufen
        raise ProcessLookupError()
    return wrapper

