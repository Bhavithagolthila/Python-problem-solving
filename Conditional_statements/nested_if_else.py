# Check whether a person is eligible to vote based on age and registration status.

age = int(input("Enter age: "))
registered = input("Are you registered? (yes/no): ").lower()

if age >= 18:
    if registered == "yes":
        print("Eligible to vote")
    else:
        print("Please register first")
else:
    print("Not eligible to vote")

    