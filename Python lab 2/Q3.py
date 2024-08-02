# Program demonstrating bitwise operators

# Print the question
print("Question 3: Write a program for bitwise operators\n")

# Define two numbers
number1 = 10  # Binary: 1010
number2 = 4   # Binary: 0100

# Bitwise AND
bitwiseAndResult = number1 & number2  # Performs AND operation on bits of number1 and number2
# 1010
# 0100
# ----
# 0000 (0 in decimal)
print("Bitwise AND:", bitwiseAndResult)

# Bitwise OR
bitwiseOrResult = number1 | number2  # Performs OR operation on bits of number1 and number2
# 1010
# 0100
# ----
# 1110 (14 in decimal)
print("Bitwise OR:", bitwiseOrResult)

# Bitwise XOR
bitwiseXorResult = number1 ^ number2  # Performs XOR operation on bits of number1 and number2
# 1010
# 0100
# ----
# 1110 (14 in decimal)
print("Bitwise XOR:", bitwiseXorResult)

# Bitwise NOT
bitwiseNotResult = ~number1  # Performs NOT operation on bits of number1
# 1010 (10 in decimal)
# ----
# 0101 (1's complement in decimal is -11 due to two's complement representation)
print("Bitwise NOT:", bitwiseNotResult)

# Bitwise Left Shift
leftShiftResult = number1 << 1  # Shifts bits of number1 to the left by 1
# 1010
# ----
# 10100 (20 in decimal)
print("Left Shift:", leftShiftResult)

# Bitwise Right Shift
rightShiftResult = number1 >> 1  # Shifts bits of number1 to the right by 1
# 1010
# ----
# 0101 (5 in decimal)
print("Right Shift:", rightShiftResult)
