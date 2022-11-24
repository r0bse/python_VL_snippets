from abc import ABC, abstractmethod


class Product(ABC):
    """
    Define the interface of objects the factory method creates
    """

    @abstractmethod
    def business_logic(self):
        pass


class Creator(ABC):
    """
    Declare the factory method, which returns an object of type Product.
    Creator may also define a default implementation of the factory
    method that returns a default ConcreteProduct object.
    Call the factory method to create a Product object
    """

    def __init__(self):
        self.product = self.factory_method()

    @abstractmethod
    def factory_method(self) -> Product:
        pass


class ConcreteCreator1(Creator):

    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self):
        return ConcreteProduct2()


class ConcreteProduct1(Product):

    def business_logic(self) -> Product:
        # TODO
        pass


class ConcreteProduct2(Product):

    def business_logic(self) -> Product:
        # TODO
        pass


if __name__ == "__main__":
    creator = ConcreteCreator1()
    product = creator.factory_method()
    product.business_logic()