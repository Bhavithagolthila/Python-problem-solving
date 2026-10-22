# If-Elif-Else 

# 1. Positive, Negative, or Zero 🔥
# Check whether a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Grade Calculation 🔥
# Display a grade based on marks (assuming marks are between 0 and 100).

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")


# 3. Simple Calculator 🔥
# Perform arithmetic based on the operator entered by the user.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    # Check for division by zero before dividing.
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# 4. Largest of Three Numbers 🔥
# Find the largest among three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# 5. Smallest of Three Numbers 🔥
# Find the smallest among three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest:", a)
elif b <= a and b <= c:
    print("Smallest:", b)
else:
    print("Smallest:", c)


# 6. Electricity Consumption Category 🔥
# Display the category based on electricity units.

units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    print("Low Consumption")
elif units <= 200:
    print("Medium Consumption")
elif units <= 300:
    print("High Consumption")
else:
    print("Very High Consumption")


# 7. Ticket Price Based on Age 🔥
# Calculate the ticket price according to age.

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket Price: ₹0")
elif age <= 17:
    print("Ticket Price: ₹100")
elif age <= 59:
    print("Ticket Price: ₹200")
else:
    print("Ticket Price: ₹150")


# 8. Leap Year Checker 🔥
# A year divisible by 400 is a leap year.
# A year divisible by 100 but not 400 is not a leap year.
# Otherwise, a year divisible by 4 is a leap year.

year = int(input("Enter year: "))

if year <= 0:
    print("Invalid year")
elif year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# 9. Vowel or Consonant 🔥
# Check whether the input is a single alphabet, vowel, or consonant.

ch = input("Enter a character: ").lower()

if len(ch) != 1 or not ch.isalpha():
    print("Invalid input")
elif ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# 10. Divisibility by Both 5 and 11 🟡
# Check whether a number is divisible by both 5 and 11.

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# 11. Triangle Type 🟡
# Validate the sides before identifying the triangle type.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid sides")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
elif a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
