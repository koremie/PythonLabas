from .binary_counter import BinaryCounter

class ReverseCounter(BinaryCounter):

    def __init__(self, name: str, price: float, count: int, is_reverse = True):
        super().__init__(name, price, count)
        self._is_reverse = is_reverse

    def __str__(self) -> str:
        return super().__str__() \
                + ", " + ("reverse" if self._is_reverse else "no reverse, not today")