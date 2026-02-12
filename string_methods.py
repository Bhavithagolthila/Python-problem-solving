# STRING IMPORTANT METHODS (Interview Ready)

s = "  Python Programming  "

# lower() – convert to lowercase
print(s.lower())

#  upper() – convert to uppercase
print(s.upper())

#  strip() – remove spaces from beginning and end
print(s.strip())

#  lstrip() – remove left spaces
print(s.lstrip())

#  rstrip() – remove right spaces
print(s.rstrip())

#  replace(old, new) – replace text
print(s.replace("Python", "Java"))

#  split() – split string into list
text = "apple,banana,orange"
print(text.split(","))

#  join() – join list into string
words = ["I", "love", "Python"]
print(" ".join(words))

#  find() – returns first index of substring
print(s.find("Python"))

#  count() – count occurrences
print(s.count("m"))

#  startswith() – check starting text
print(s.startswith("  Py"))

#  endswith() – check ending text
print(s.endswith("  "))

#  isalpha() – check if only letters
print("Hello".isalpha())

#  isdigit() – check if only numbers
print("1234".isdigit())

#  isalnum() – check letters + numbers
print("Python123".isalnum())

#  capitalize() – first letter uppercase
print("python".capitalize())

#  title() – first letter of each word uppercase
print("python programming".title())

# swapcase() – swap uppercase/lowercase
print("PyThOn".swapcase())
