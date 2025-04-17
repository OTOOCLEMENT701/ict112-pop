"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.

original_string = "Programming"
reversed_string = original_string[::-1]
print(reversed_string)

2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."

# Get user input
full_name = input("Enter your full name: ")
# Split the name into parts
name_parts = full_name.split()
# Extract initials and format them
initials = [part[0].upper() + '.' for part in name_parts]
# Join the initials and print
print(''.join(initials))

3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c for c in s.lower() if c.isalnum())
    return s == s[::-1]
# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome!")
else:
    print(f"'{input_string}' is not a palindrome.")
"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.

# Ask the user for input
sentence = input("Enter a sentence: ")
# Split the sentence into words (split by whitespace by default)
words = sentence.split()
# Count the number of words
word_count = len(words)
# Display the result
print(f"Number of words in the sentence: {word_count}")

5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.

original_string = "This is a string and it is an example."
modified_string = original_string.replace(" is ", " was ")  # Replace with spaces to avoid partial matches
print(modified_string)
