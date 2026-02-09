t = (10, 20, 30)

# Convert tuple to list
l = list(t)

# Modify list
l[1] = 99
l.append(40)

# Convert back to tuple
t = tuple(l)

print(t)
