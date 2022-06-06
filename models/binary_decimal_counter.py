from .binary_counter import BinaryCounter

class BinaryDecimalCounter(BinaryCounter):

    def __init__(self, name: str, price: float, count: int, decimal_lol = True):
        super().__init__(name, price, count)
        self._decimal_lol = decimal_lol

    def __str__(self) -> str:
        return super().__str__() \
                    + ", decimal-lol?: " + ("yaas" if self._decimal_lol else "no")