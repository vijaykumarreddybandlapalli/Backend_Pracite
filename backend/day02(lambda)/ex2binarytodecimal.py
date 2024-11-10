

binary_num = input("Enter a binary number: ")
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):
        decimal =decimal+int(digit) * (2 ** power)
        power += 1
    return decimal


print("Decimal equivalent:", binary_to_decimal(binary_num))