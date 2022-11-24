import copy

class Prototype:
    pass

def main():
    prototype = Prototype()
    prototype_copy = copy.deepcopy(prototype)

if __name__ == "__main__":
    main()