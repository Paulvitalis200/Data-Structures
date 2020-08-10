"""
Use a stack data structure to convert integer values to binary.

Example: 242

242 / 2 = 121 rem 0

121 / 2 = 60 rem 1

60 / 2 = 30 rem 0

30 / 2 = 15 rem 0

15 / 2 = 7 rem 1

7 / 2 = 3 rem 1

3 / 2 = 1 rem 1

1 / 2 = 0 rem 1

int('1111010', 2) = 242
"""

from stacks import Stack


def div_by_two(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(div_by_two(242))

