from .device import Device

class RsTrigger(Device):

    def __init__(self, name: str, price: float, state: bool):
        super().__init__(name, price)
        self._state = state
        
    def __str__(self) -> str:
        return super().__str__() + f", device's state: {self._state}"