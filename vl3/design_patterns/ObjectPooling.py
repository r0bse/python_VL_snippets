class Reusable():
    """
    Collaborate with other objects for a limited amount of time,
    then they are no longer needed for that collaboration
    """
    pass


class ReusablePool:
    """
    Manage reusable objects to be used by Clients
    """

    def __init__(self, size):
        self._reusabels = (Reusable() for _ in range(size))

    def aquire(self):
        return self._reusabels.pop()

    def release(self, reusable: Reusable):
        self._reusabels.append(reusable)


if __name__ == "__main__":
    reusable_pool = ReusablePool(10)
    reusable = reusable_pool.aquire()

    # Do something with the object

    reusable_pool.release(reusable)