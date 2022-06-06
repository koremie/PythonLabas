from audioop import mul
from models.binary_counter import BinaryCounter
from models.binary_decimal_counter import BinaryDecimalCounter
from models.reverse_counter import ReverseCounter
from models.d_trigger import DTrigger
from models.rs_trigger import RsTrigger
from models.multiplexer import Multiplexer
from models.shifting_register import ShiftingRegister

def main():
    b_counter = BinaryCounter('binary counter', 499, 76590)
    b_d_counter = BinaryDecimalCounter('binary-decimal counter', 799, 45638)
    reverse_counter = ReverseCounter('reverse counter', 999, 43210, False)
    d_trigger = DTrigger('D-trigger', 1999.99, False, False)
    rs_trigger = RsTrigger('RS-trigger', 599, True)
    multiplexer = Multiplexer('multiplexer', 659, 77)
    shifting_reg = ShiftingRegister('shifting register', 3899)
    device_list = [b_counter, b_d_counter, reverse_counter, 
            d_trigger, rs_trigger, multiplexer, shifting_reg]
    print(*device_list, sep='\n')

if __name__ == '__main__':
    main()