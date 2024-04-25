class SimpleClass:
    def __init__(self, value: str = ""):
        self.string = value

    def say_hello(self):
        print("Hello " + self.string)

    def create_instance_variable_example(self, value: str):
        self.example = value

if __name__ == "__main__":
    simpleClass = SimpleClass("initiated in constructor")
    print(simpleClass.string)
    simpleClass.say_hello()
    # print(simpleClass.example)
    simpleClass.create_instance_variable_example("foo")
    print(simpleClass.example)