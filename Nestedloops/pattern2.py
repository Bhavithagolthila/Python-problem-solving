"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""

for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")  # if we write i here it prints the value of i in each row
    print()    # move to next line after inner loop is completed