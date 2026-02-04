age = int(input("Enter age: "))
citizen = input("Are you Indian? (yes/no): ")

if age >= 18:
    if citizen == "yes":
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Underage")
