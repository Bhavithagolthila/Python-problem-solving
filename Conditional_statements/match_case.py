# Simple calculator

a = 10
b = 5
operator = "+"

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")


# Combine multiple cases with |
day = 6
match day:
    case 6 | 7:
        print("Weekend")
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case _:
        print("Invalid day")


# Menu selection
choice = 2
match choice:
    case 1:
        print("View profile")
    case 2:
        print("Update profile")
    case 3:
        print("Logout")
    case _:
        print("Invalid choice")

# Traffic light

color = "green"
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color")


# Vowel or consonant (uses | and .lower())

ch = "E"
match ch.lower():
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _:
        print("Consonant")

# HTTP status code

code = 404
match code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")


# Type checker (class pattern)

value = 3.14
match value:
    case int():
        print("Integer")
    case float():
        print("Float")
    case str():
        print("String")
    case list():
        print("List")
    case _:
        print("Other")




                   