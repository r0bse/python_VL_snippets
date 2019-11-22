import examples.scopes.scope1 as scope1
import examples.scopes.scope2 as scope2

some_string = "Some String in module {0}".format(__name__)

if __name__ == "__main__":
    print(some_string)
    print(scope1.some_string)
    print(scope2.some_string)

