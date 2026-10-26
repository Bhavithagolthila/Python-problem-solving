# Skip multiples of 5 from 1 to 30
for i in range(1, 31):
    if i % 5 == 0:
        continue
    print(i, end=" ")

# Skip negative numbers
numbers = [10, -5, 20, -2, 30]
for num in numbers:
    if num < 0:
        continue
    print(num)

# Skip the number 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")

# Print odd numbers from 1 to 20 using continue
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")
