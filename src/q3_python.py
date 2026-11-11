# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName):
    # Remove stray spaces, then capitalise each name
    # (first letter uppercase, the rest lowercase), e.g. "bob" -> "Bob"
    first = firstName.strip().capitalize()
    last = lastName.strip().capitalize()

    # Put them together as "lastName, firstName"
    return f"{last}, {first}"


# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):
     # Take the first character of each name and make it uppercase.
    # .upper() means the input's case doesn't matter.
    firstInitial = firstName.strip()[0].upper()
    lastInitial = lastName.strip()[0].upper()

    # Put a full stop after each initial, e.g. "J.S."
    return f"{firstInitial}.{lastInitial}."


# Task 3:
# Call both functions with the following inputs and print each result:
#   formatName("Alice", "Tan")  → Expected: "Tan, Alice"
#   formatName("bob", "lim")    → Expected: "Lim, Bob"
#   formatInitials("Alice","Tan") → Expected: "A.T."
#   formatInitials("bob","lim")   → Expected: "B.L."

print(formatName("Alice", "Tan"))      # Tan, Alice
print(formatName("bob", "lim"))        # Lim, Bob
print(formatInitials("Alice", "Tan"))  # A.T.
print(formatInitials("bob", "lim"))    # B.L.
