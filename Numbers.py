age = 30 # integer
print(age)
print(30)

PI = 3.14159 # float
# this is a hash sign
RADIANS_TO_DEGREES = 180 / PI # Fixed 
print(RADIANS_TO_DEGREES)

# Arithmetic Operations
# PEMDA or BODMAS rules
# Brackets, Orders, Division, Multiplication, Addition & Subtraction
maths_operations = 1 + 3 * 4 / 2 - 2
print(maths_operations)

# Whenever you do normal divison, you always get back a float e.g 5.0

float_divison = 12 / 3
print(float_divison)

float_divison2 = 8 / 3
print(float_divison2)

# To get rid of the floating point/ decimal place, do integer float_divison 
# // performs the division and just removes everything after the decimal place; does not round up/down 
integer_division = 12 // 3
print(integer_division)

integer_division2 = 8 // 3
print(integer_division2)

# find whether a number is odd or even using remainder of normal divison or modulus operator 
# 5 goes into 13 twice so answer is 2
division1 = 13 // 5
print(division1)
# To get remainder of division1 (which is 3), we use modulus % operator
remainder = 13 % 5
print(remainder)

# 10 / 21
# 14 / 2
# 6 / 2
# 340 / 2
# All of these numbers are Even
# Remainder of division by 2 is always 0 for even numbers

# 11 / 2
# 27 / 2
# 3 / 2
# All of these numbers are Odd
# Remainder of division by 2 is always 1 for odd numbers