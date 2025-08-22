# Assignment 2 – REE 200 & PET ENG 200
# Solution by ChatGPT

import math
import string

# -------------------------
# Task 1: Convert to lowercase
# -------------------------
def to_lowercase(s):
    return s.lower()

# -------------------------
# Task 2: Swap case
# -------------------------
def swap_case(s):
    return s.swapcase()

# -------------------------
# Task 3: Remove uppercase letters
# -------------------------
def remove_uppercase(s):
    return ''.join([ch for ch in s if not ch.isupper()])

# -------------------------
# Task 4: Count uppercase and lowercase
# -------------------------
def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return f"Uppercase: {upper}, Lowercase: {lower}"

# -------------------------
# Task 5: Remove non-English letters
# -------------------------
def remove_non_letters(s):
    return ''.join([ch for ch in s if ch.isalpha()])

# -------------------------
# Task 6: Triangle area using Heron’s formula
# -------------------------
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# -------------------------
# Task 7: Format names neatly in a table
# -------------------------
def format_names(names):
    print("Name".ljust(20), "Length".rjust(10))
    print("-" * 30)
    for name in names:
        print(name.ljust(20), str(len(name)).rjust(10))

# -------------------------
# Task 8: Clean a string
# -------------------------
def clean_string(s):
    s = s.strip()
    s = ''.join(ch for ch in s if ch not in string.punctuation)
    s = s.replace(" ", "")
    return s

# -------------------------
# MAIN PROGRAM
# -------------------------
if __name__ == "__main__":
    print("Task 1:", to_lowercase("Hello"))
    print("Task 2:", swap_case("HeLLo WoRLd"))
    print("Task 3:", remove_uppercase("HelloWorld"))
    print("Task 4:", count_case("EngiNEEr"))
    print("Task 5:", remove_non_letters("Data-Driven@2025!"))
    print("Task 6:", triangle_area(3, 4, 5))

    print("\nTask 7:")
    format_names(["Alice", "Bob", "Catherine", "David"])

    print("\nTask 8:", clean_string("   Hello, World!    "))
