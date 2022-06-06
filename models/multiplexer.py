from .device import Device

class Multiplexer(Device):

    def __init__(self, name: str, price: float, multi: int):
        super().__init__(name, price)
        self._multi = multi

    def __str__(self) -> str:
        return super().__str__() + f", device's multi: {self._multi}"