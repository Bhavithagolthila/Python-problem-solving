# print numbers from 1 to 10 and break the loop when number is 5
for i in range(1, 11):
    if i == 5:  # execute till 5 and then break the loop
        break
    print(i)

#  Find a number in a list and stop searching
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 40:
        print("Found")
        break

#  Print numbers until the user enters 0
while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break

    print(num)

#  Stop when the first even number is found
numbers = [1, 3, 5, 8, 10, 12]
for num in numbers:
    if num % 2 == 0:
        print("First even number:", num)
        break

#  Print multiplication table values and stop at 5
for i in range(1, 11):
    if i == 6:
        break
    print(5 * i)


