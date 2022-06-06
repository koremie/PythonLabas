from .device import Device

class BinaryCounter(Device):

    def __init__(self, name: str, price: float, count: int):
        super().__init__(name, price)
        self._count = count

    def __str__(self) -> str:
        return super().__str__() + f", device's count: {self._count}"
