
# ============================================================
# PYTHON IF STATEMENT
# ============================================================


# ------------------------------------------------------------
# 1. WHAT IS AN IF STATEMENT?
# ------------------------------------------------------------
# An if statement is a conditional statement that executes
# a block of code only when the given condition is True.


# ------------------------------------------------------------
# 2. WHY IS AN IF STATEMENT USED?
# ------------------------------------------------------------
# 1. To make decisions in a program.
# 2. To check whether a condition is True or False.
# 3. To execute code only when a condition is satisfied.
# 4. To control the flow of a program.


# ------------------------------------------------------------
# 3. SYNTAX OF AN IF STATEMENT
# ------------------------------------------------------------
# if condition:
#     statement
#
# The colon (:) is required after the condition.
# The statement inside the if block must be indented.
# Python conventionally uses four spaces for indentation.


# ------------------------------------------------------------
# 4. HOW DOES AN IF STATEMENT WORK?
# ------------------------------------------------------------
# 1. Python checks the condition.
# 2. If the condition is True, the indented code executes.
# 3. If the condition is False, the indented code is skipped.
# 4. The program continues with the next statement.


# ------------------------------------------------------------
# 5. REAL-LIFE EXAMPLE
# ------------------------------------------------------------
# If a person is 18 years old or older, they are eligible
# to vote.
#
# If the age is less than 18, the if block is skipped.


# ------------------------------------------------------------
# 6. CHECK WHETHER A NUMBER IS POSITIVE
# ------------------------------------------------------------
# Question:
# Take a number. Print "Positive" if it is greater than 0.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")


# ------------------------------------------------------------
# 7. CHECK VOTING ELIGIBILITY
# ------------------------------------------------------------
# Question:
# Take an age. Print "Eligible to vote" if age is 18 or more.

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")


# ------------------------------------------------------------
# 8. CHECK WHETHER A NUMBER IS EVEN
# ------------------------------------------------------------
# Question:
# Take a number. Print "Even" if it is divisible by 2.
#
# The % operator returns the remainder.
# If num % 2 == 0, the number is even.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")


# ------------------------------------------------------------
# 9. CHECK WHETHER A STUDENT PASSED
# ------------------------------------------------------------
# Question:
# Take marks. Print "Pass" if marks are 35 or more.

marks = int(input("Enter your marks: "))

if marks >= 35:
    print("Pass")


# ------------------------------------------------------------
# 10. CHECK A PASSWORD
# ------------------------------------------------------------
# Question:
# Print "Access granted" if the password is "python123".

password = input("Enter your password: ")

if password == "python123":
    print("Access granted")


# ------------------------------------------------------------
# 11. PREDICT THE OUTPUT - FALSE CONDITION
# ------------------------------------------------------------
# Question:
# What is the output?

x = 5
if x > 10:
    print("A")
print("B")

# Output:
# B

# Explanation:
# The condition 5 > 10 is False.
# Therefore, print("A") is skipped.
# print("B") is outside the if block, so it executes.


# ------------------------------------------------------------
# 12. PREDICT THE OUTPUT - TRUE CONDITION
# ------------------------------------------------------------
# Question:
# What is the output?

x = 12
if x > 10:
    print("A")
print("B")

# Output:
# A
# B

# Explanation:
# The condition 12 > 10 is True.
# Therefore, "A" is printed.
# "B" is outside the if block, so it also prints.


# ------------------------------------------------------------
# 13. CONVERT A NEGATIVE NUMBER TO POSITIVE
# ------------------------------------------------------------
# Question:
# Take a number. If it is negative, convert it to positive.
# Then print the absolute value.
#
# We use only if and do not use the built-in abs() function.

num = int(input("Enter a number: "))

if num < 0:
    num = -num

print("Absolute value:", num)


# ------------------------------------------------------------
# 14. CHECK WHETHER A NUMBER IS DIVISIBLE BY 5
# ------------------------------------------------------------
# Question:
# Print "Divisible by 5" if the number is divisible by 5.

num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")


# ------------------------------------------------------------
# 15. CHECK WHETHER A NUMBER IS GREATER THAN 100
# ------------------------------------------------------------
# Question:
# Print "Greater than 100" if the number is above 100.

num = int(input("Enter a number: "))

if num > 100:
    print("Greater than 100")


# ------------------------------------------------------------
# 16. CHECK WHETHER A NUMBER IS DIVISIBLE BY 3
# ------------------------------------------------------------
# Question:
# Print "Divisible by 3" if the number is divisible by 3.

num = int(input("Enter a number: "))

if num % 3 == 0:
    print("Divisible by 3")


# ------------------------------------------------------------
# 17. CHECK DISCOUNT ELIGIBILITY
# ------------------------------------------------------------
# Question:
# Print "Discount available" if the purchase amount is 1000
# or more.

amount = float(input("Enter purchase amount: "))

if amount >= 1000:
    print("Discount available")


# ------------------------------------------------------------
# 18. CHECK WHETHER A NUMBER IS NEGATIVE
# ------------------------------------------------------------
# Question:
# Print "Negative" if the number is less than 0.

num = int(input("Enter a number: "))

if num < 0:
    print("Negative")


# ------------------------------------------------------------
# 19. CHECK WHETHER A NUMBER IS ZERO
# ------------------------------------------------------------
# Question:
# Print "Zero" if the number is equal to 0.

num = int(input("Enter a number: "))

if num == 0:
    print("Zero")


# ------------------------------------------------------------
# 20. INCREASE AN ODD NUMBER BY ONE
# ------------------------------------------------------------
# Question:
# If a number is odd, increase it by one and print the result.

num = int(input("Enter a number: "))

if num % 2 != 0:
    num = num + 1

print("Result:", num)


# ============================================================
# INTERVIEW THEORY QUESTIONS AND ANSWERS
# ============================================================

# Q1. What is an if statement?
# Answer:
# An if statement executes a block of code only when the
# given condition is True.


# Q2. Why do we use an if statement?
# Answer:
# We use it to make decisions and execute code when a
# specific condition is satisfied.


# Q3. What happens when an if condition is False?
# Answer:
# The code inside the if block is skipped.


# Q4. What is indentation in Python?
# Answer:
# Indentation means spaces at the beginning of a line.
# It defines a block of code in Python.
# Four spaces are conventionally used for each indentation level.


# Q5. What is the difference between = and ==?
# Answer:
# = assigns a value to a variable.
# == compares two values to check whether they are equal.


# Q6. What does the % operator do?
# Answer:
# The modulo operator (%) returns the remainder after division.


# Q7. Can we use an if statement without else?
# Answer:
# Yes. An if statement can be used independently.


# Q8. What is a Boolean condition?
# Answer:
# A Boolean condition evaluates to True or False.


# Q9. What happens to code outside an if block?
# Answer:
# It executes normally, regardless of whether the condition
# is True or False.


# Q10. How do you check whether a number is even?
# Answer:
# Use if num % 2 == 0 to check whether the remainder is zero.


# ============================================================
# IMPORTANT POINTS TO REMEMBER
# ============================================================

# 1. Use a colon (:) after the if condition.
# 2. Indent the code inside the if block.
# 3. Use == to compare two values.
# 4. Use % to check divisibility.
# 5. If the condition is False, the if block is skipped.
# 6. Code outside the if block can still execute.
# 7. An if statement does not automatically print anything.
# 8. Practise predicting the output of code.
#
# IMPORTANT:
# This file contains multiple input() statements.
# When you run it, enter the requested values one by one.
# Each section runs in sequence.
# ============================================================
