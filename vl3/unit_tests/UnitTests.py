import unittest

class Foo:
    def __init__(self):
        self.value = True


class Bar:
    def __init__(self):
        self.value = False


class MyTestCase(unittest.TestCase):

    def test_Foo(self):
        foo = Foo()
        self.assertTrue(foo.value)

    def test_Bar(self):
        bar = Bar()
        self.assertIsInstance(bar.value, "das hier steht dann da wenn der Test umfällt")
