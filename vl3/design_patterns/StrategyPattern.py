from abc import ABC, abstractmethod


class FlexibleObject():
    """
    define the interface of interest
    and maintain a reference to the strategy object
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def strategy_method(self):
        self._strategy.strategy_method()


class Strategy(ABC):
    """
    Declare an interface common to all supported lgorithms.
    Context uses this interface to call the algorithm defined
    by a concrete strategy
    """

    @abstractmethod
    def strategy_method(self):
        pass


class ConcreteStrategy1(Strategy):

    def strategy_method(self):
        print("Concrete Strategy 1")


class ConcreteStrategy2(Strategy):

    def strategy_method(self):
        print("Concrete Strategy 2")


if __name__ == "__main__":

    flexible_object = FlexibleObject(ConcreteStrategy1())
    flexible_object.strategy_method()
    flexible_object._strategy = ConcreteStrategy2()
    flexible_object.strategy_method()