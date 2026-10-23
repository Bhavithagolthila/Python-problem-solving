# last digit of a number
n = 4905
last = n % 10
print(last)

# Count digits (🔥)
n = 4905
count = 0
while n > 0:
    count = count + 1
    n = n // 10
print(count)


#  First digit (🔥)
n = 4905
while n >= 10:
    n = n // 10
print(n)

# reverse a number (🔥)
n = 4905
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print(rev)

# Palindrome number (🔥)
n = 121
original = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if rev == original:
    print("Palindrome")
else:
    print("Not a palindrome")

    