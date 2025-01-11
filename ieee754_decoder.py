import struct
from dataclasses import dataclass

@dataclass
class IEEE754Float:
    sign: int
    exponent: int 
    mantissa: int
    binary: str

    @classmethod
    def from_float(cls, num: float) -> 'IEEE754Float':
        packed = struct.pack('!f', num)
        binary = ''.join(format(byte, '08b') for byte in packed)
        
        return cls(
            sign=int(binary[0]),
            exponent=int(binary[1:9], 2),
            mantissa=int(binary[9:], 2),
            binary=binary
        )

    def get_actual_exponent(self) -> int:
        return self.exponent - 127

    def get_mantissa_value(self) -> float:
        mantissa_value = 1.0
        for i in range(23):
            if self.mantissa & (1 << (22 - i)):
                mantissa_value += 2 ** -(i + 1)
        return mantissa_value

    def to_float(self) -> float:
        return (-1) ** self.sign * self.get_mantissa_value() * (2 ** self.get_actual_exponent())

    def get_mantissa_terms(self) -> list[str]:
        trimmed_mantissa = self.binary[9:].rstrip('0')
        return [f"{trimmed_mantissa[i]}*2^{-i-1}" for i in range(len(trimmed_mantissa))]

    def __str__(self) -> str:
        mantissa_sum = 1 + sum(
            int(self.binary[9+i]) * (2 ** (-i-1)) 
            for i in range(len(self.binary[9:].rstrip('0')))
        )
        
        return (
            f"Binary representation of {self.binary}\n"
            f"Sign: {'+ ' if self.sign == 0 else '- '}\n"
            f"Exponent: {self.binary[1:9]} = {self.get_actual_exponent()}\n"
            f"Mantissa: {self.binary[9:]}\n"
            f"Mantissa deconstructed to be: {' + '.join(self.get_mantissa_terms())}"
            f"{' + trailing 0s' if len(self.binary[9:].rstrip('0')) < 23 else ''} = {mantissa_sum-1}\n"
            f"Plus the implicit 1: {mantissa_sum}\n"
            f"Final value: {'+1' if self.sign == 0 else '-1'}*2^{self.get_actual_exponent()}"
            f"*{mantissa_sum} = {self.to_float()}"
        )

@dataclass
class IEEE754Double:
    sign: int
    exponent: int 
    mantissa: int
    binary: str

    @classmethod
    def from_double(cls, num: float) -> 'IEEE754Double':
        packed = struct.pack('!d', num)  # 'd' for double precision
        binary = ''.join(format(byte, '08b') for byte in packed)
        
        return cls(
            sign=int(binary[0]),
            exponent=int(binary[1:12], 2),  # 11 bits for exponent in double
            mantissa=int(binary[12:], 2),   # 52 bits for mantissa in double
            binary=binary
        )

    def get_actual_exponent(self) -> int:
        return self.exponent - 1023  # Bias is 1023 for double precision

    def get_mantissa_value(self) -> float:
        mantissa_value = 1.0
        for i in range(52):  # 52 bits for mantissa
            if self.mantissa & (1 << (51 - i)):  # 51 instead of 22
                mantissa_value += 2 ** -(i + 1)
        return mantissa_value

    def to_double(self) -> float:
        return (-1) ** self.sign * self.get_mantissa_value() * (2 ** self.get_actual_exponent())

    def get_mantissa_terms(self) -> list[str]:
        trimmed_mantissa = self.binary[12:].rstrip('0')  # Start from bit 12
        return [f"{trimmed_mantissa[i]}*2^{-i-1}" for i in range(len(trimmed_mantissa))]

    def __str__(self) -> str:
        mantissa_sum = 1 + sum(
            int(self.binary[12+i]) * (2 ** (-i-1)) 
            for i in range(len(self.binary[12:].rstrip('0')))
        )
        
        return (
            f"Binary representation of {self.binary}\n"
            f"Sign: {'+ ' if self.sign == 0 else '- '}\n"
            f"Exponent: {self.binary[1:12]} = {self.get_actual_exponent()}\n"
            f"Mantissa: {self.binary[12:]}\n"
            f"Deconstructed: {' + '.join(self.get_mantissa_terms())}"
            f"{' + trailing 0s' if len(self.binary[12:].rstrip('0')) < 52 else ''}\n"
            f"With implicit 1: {mantissa_sum}\n"
            f"Final value: {'+1' if self.sign == 0 else '-1'}*2^{self.get_actual_exponent()}"
            f"*{mantissa_sum} = {self.to_double()}"
        )

def main():
    # float_number = 5.75
    # ieee754 = IEEE754Float.from_float(float_number)

    double_number = 5.75
    ieee754 = IEEE754Double.from_double(double_number)

    print(ieee754)

if __name__ == '__main__':
    main()