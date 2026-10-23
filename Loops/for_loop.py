for i in range(3):
    print("Python is fun")

for i in range(7):
    print("Python is fun")

for fruit in ["Apple", "Banana", "Mango"]:  # list of fruits
    print(fruit)      

for city in ["Delhi", "Mumbai"]: 
    print("I love", city) #  output: I love Delhi and I love Mumbai

for name in ["Ravi", "Sita", "Arjun"]: # output: Hello Ravi, Hello Sita, Hello Arjun
    print("Hello", name)

for fruit in ["Apple", "Mango"]:
    print(fruit)
    print("Good fruit") # output: Apple Good fruit Mango Good fruit

for fruit in ["Apple", "Mango"]:
    print(fruit)
print("Good fruit") # output: Apple Mango Good fruit

# Write Python code to print numbers from 1 to 10 using a for loop and range().
for i in range(1, 11):  
    print(i, end=" ")  # output: 1 2 3 4 5 6 7 8 9 10

# Print numbers in reverse order
for i in range(10, 0, -1):  
    print(i)  

# Print even numbers
for i in range(2, 21, 2):
    print(i)  # output: 2 4 6 8 10 12 14 16 18 20

# Print odd numbers
for i in range(1, 20, 2):
    print(i)  # output: 1 3 5 7 9 11 13 15 17 19


# 🔥Find the sum of numbers from 1 to 10 
total = 0
for i in range(1, 11):
    total = total + i
print(total)

# 🔥Multiplication table
n = 5
for i in range(1, 11):
        print(f"{n} x {i} = {n*i} ")


# Count characters without len()  text = "Python"

text = "Python"
count = 0
for ch in text:
    count = count + 1
print(count)

# 🔥Count vowels in a string
text ="Education".lower()
count = 0
for ch in text:
    if ch in 'aeiou':
        count = count + 1
print(count)

# 🔥Sum of numbers in a list
nums = [10, 20, 30, 40, 50]
total = 0
for num in nums:
    total = total + num
print(total)

# 🔥 Print each number with its index
nums = [10, 20, 30, 40, 50]
for i in range(len(nums)):
    print(f"Index {i}: {nums[i]}")

# Largest number in a list
nums = [10, 45, 23, 78, 12]
largest = nums[0]
for i in range(len(nums)):
    if largest < nums[i]:
        largest = nums[i]  
print(largest)   

# or
nums = [10, 45, 23, 78, 12]
largest = max(nums)
print(largest)

# or
nums = [10, 45, 23, 78, 12]
largest = nums[0]
for num in nums:
    if largest < num:
        largest = num
print(largest)   

# count even numbers in a list
nums = [10, 15, 20, 25, 30, 35, 40]
count = 0  # Hint: initialize the counter
for num in nums:
    if num % 2 == 0:
        count = count + 1
print(count)


# Reverse a string using a for loop
text = "Python"
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print(reversed_text)

# 🔥Find the smallest number in a list

nums = [25, 10, 45, 5, 30]
smallest = nums[0]
for num in nums:
    if smallest > num:
        smallest = num
print(smallest)

#  Count positive numbers in a list
nums = [-5, 10, -2, 8, 0, 15, -1]
count = 0
for num in nums:
    if num > 0:
        count = count + 1
print(count)

#  Count negative numbers in a list
nums = [-5, 10, -2, 8, 0, 15, -1]
count = 0
for num in nums:
    if num < 0:
        count = count + 1
print(count)





