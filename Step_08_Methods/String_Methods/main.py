# STRING METHODS
# String methods are used to manipulate strings in Python. These methods are called on the string itself.

name = "Hadiqa Gohar"
print(name)  # Output: Hadiqa Gohar

# 1. upper(): Converts all characters in the string to uppercase.
uppercase = name.upper()
print(uppercase)  # Output: HADIQA GOHAR

# 2. lower(): Converts all characters in the string to lowercase.
lowercase = name.lower()
print(lowercase)  # Output: hadiqa gohar

# 3. capitalize(): Converts the first character of the string to uppercase, rest to lowercase.
capitalized = name.capitalize()
print(capitalized)  # Output: Hadiqa gohar

# 4. strip(): Removes any leading and trailing spaces from the string.
striped = name.strip()
print(striped)  # Output: Hadiqa Gohar (No extra spaces to strip here)

# 5. replace(): Replaces occurrences of a substring with another.
replaced = name.replace("Hadiqa", "Hello")
print(replaced)  # Output: Hello Gohar (Hadiqa replaced with Hello)

# 6. title(): Converts the first character of each word to uppercase.
tilted = name.title()
print(tilted)  # Output: Hadiqa Gohar

# 7. split(): Splits the string into a list based on spaces.
split = name.split()
print(split)  # Output: ['Hadiqa', 'Gohar']

# 8. join(): Joins list elements into a string with a separator.
joined = " _ ".join(split)
print(joined)  # Output: Hadiqa _ Gohar

# 9. find(): Finds the index of the first occurrence of a substring.
find = name.find("Gohar")
print(find)  # Output: 7 (index where "Gohar" starts)

# 10. count(): Counts how many times a character appears in the string.
count = name.count("a")
print(count)  # Output: 3
