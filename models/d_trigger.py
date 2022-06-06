from .rs_trigger import RsTrigger

class DTrigger(RsTrigger):

    def __init__(self, name: str, price: float, state: bool, d_lol = True):
        super().__init__(name, price, state)
        self._d_lol = d_lol

    def __str__(self) -> str:
        return super().__str__() \
                    + ", D-lol?: " + ("yaas" if self._d_lol else "no")