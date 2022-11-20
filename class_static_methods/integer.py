import math


class Integer:

    def __init__(self,value):
        self.value = value

    @classmethod
    def from_float(cls,float_value):
        if type(float_value) is not float:
            return "value is not a float"
        return cls(math.floor(float_value))
    @classmethod
    def from_roman(cls,value):
        rom_nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        if len(value) <=1:
            return rom_nums[value]
        else:
            for i in range(len(value)):
                if 