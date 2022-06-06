from abc import ABC

class Device(ABC):

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price
        
    def __str__(self) -> str:
        return f"Device's name: {self._name}, price: {self._price}"
