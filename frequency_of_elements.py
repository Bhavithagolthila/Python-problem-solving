lst = [1, 2, 2, 3, 3, 3]
freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print(freq)
