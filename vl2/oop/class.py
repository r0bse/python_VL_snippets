
class SimpleClass:

    def __init__(self, value: str = ""):
        self.example = None
        self.string = value

    def say_hello(self, value):
        print("Hello {0}".format(value))

    def create_instance_variable_example(self, value: str):
        self.example = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "SimpleClass({0})".format(self.string)

simple_class = SimpleClass()
simple_class.say_hello("world")

print(SimpleClass())
print(SimpleClass("something, something"))

simple_class = SimpleClass("something, something")
simple_class.create_instance_variable_example("foo")
print(simple_class.example)