from .device import Device

class ShiftingRegister(Device):

    def __init__(self, name: str, price: float, is_shifting = True):
        super().__init__(name, price)
        self._is_shifting = is_shifting

    def __str__(self) -> str:
        return super().__str__() \
                + ", " + ("yaas it's a ShiFtINg reG1stEer" if self._is_shifting else "TwT")