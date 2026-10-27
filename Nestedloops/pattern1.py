"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(1,6):
        print(j,end=" ") # if we write j here it prints the value of j in each row
    print()   # move to next line after inner loop is completed 