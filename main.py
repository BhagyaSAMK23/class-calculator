# main.py
from modules import addition
from modules import subtraction
from modules import multiplication
from modules import squareroot

print("Using addition:")
print("1 + 2 =", addition.add_two_numbers(1, 2))

print("Using subtraction:")
print("5 - 3 =", subtraction.subtract_two_numbers(5, 3))

print("Using multiplication:")
print("4 * 3 =", multiplication.multiply_two_numbers(4, 3))

print("Using square root:")
print("Square root of 16 =", squareroot.square_root_of_number(16))
