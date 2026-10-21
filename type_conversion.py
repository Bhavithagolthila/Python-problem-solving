# Python Type Conversion
# ======================
#
# Definition:
# Type conversion is the process of changing a value from one data type
# to another data type.
#
# There are two commonly taught types:
# 1. Implicit Type Conversion
# 2. Explicit Type Conversion


# 🔥 1. Explicit Type Conversion
# ------------------------------
# Definition:
# Explicit type conversion happens when the programmer manually
# converts a value from one data type to another using functions
# such as int(), float(), str(), and bool().


# Q1. Convert string to integer
num = "25"
num1 = int(num)

print(num1)
print(type(num1))


# Q2. Convert integer to float
num = 10
num2 = float(num)

print(num2)
print(type(num2))


# Q3. Convert integer to string
num = 100
num3 = str(num)

print(num3)
print(type(num3))


# 🟡 2. Type Conversion with Calculations
# ---------------------------------------


# Q4. Convert string to integer and add
a = "20"
b = 10

c = int(a)
result = c + b

print(result)


# Q5. Convert float to integer
price = 99.9
result = int(price)

print(result)  # 99 (the decimal part is removed, not rounded)


# Q6. Convert numbers to Boolean values
a = bool(0)
b = bool(1)

print(a, b)  # False True


# 🔥 3. Implicit Type Conversion
# ------------------------------
# Definition:
# Implicit type conversion happens when Python automatically
# converts a value from one data type to another during an operation.


# Q7. Addition of an integer and a float
a = 5
b = 2.5

result = a + b

print(result)        # 7.5
print(type(result))  # <class 'float'>


# Q8. Multiplication of an integer and a float
a = 4
b = 3.5

result = a * b

print(result)        # 14.0
print(type(result))  # <class 'float'>


# 🔥 Important Interview Difference
# ---------------------------------
# Implicit conversion: Python converts the data type automatically.
# Explicit conversion: The programmer converts the data type manually.