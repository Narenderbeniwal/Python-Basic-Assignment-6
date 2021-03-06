# -*- coding: utf-8 -*-
"""Python Basic Assignment 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vYvYZ4e-jAFOMKtPjCUHQHd_n1KzjC3v

Q. 1. What are escape characters, and how do you use them?

Solution: In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return. Conversely, prefixing a special character with "\" turns it into an ordinary character.

Q 2. What do the escape characters n and t stand for?

Sol: : "\t" is a tab, "\n" is a newline

Q. 3. What is the way to include backslash characters in a string?

Sol: Use two backslashes to represent a backslash

Use the syntax "\\**\**" within the string literal to represent a single backslash.

Q 4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?

Sol: The single quote in Howl's is fine because you've used double quotes to mark the beginning and end of the string.

Q. 5. How do you write a string of newlines if you don't want to use the n character?


Sol: Multiline strings allow you to use newlines in strings without the \n escape character.
"""

## 6. What are the values of the given expressions?
###'Hello, world!'[1]
#'Hello, world!'[0:5]
#'Hello, world!'[:5]
#'Hello, world!'[3:] 
# Sol: 
print('Hello, world!'[1])
print('Hello, world!'[0:5])
print('Hello, world!'[:5])
print('Hello, world!'[3:])

#7. What are the values of the following expressions?
#'Hello'.upper()
#'Hello'.upper().isupper()
# 'Hello'.upper().lower()
# Sol: 
print('Hello'.upper())
print('Hello'.upper().isupper())
print('Hello'.upper().lower())

# 8. What are the values of the following expressions?
#'Remember, remember, the fifth of July.'.split()
# '-'.join('There can only one.'.split())
# Sol: 
print('Remember, remember, the fifth of July.'.split())
print('-'.join('There can only one.'.split()))

# Q. 9. What are the methods for right-justifying, left-justifying, and centering a string?
# Sol: The rjust(), ljust() and center() strings methods.



# Q. 10. What is the best way to remove whitespace characters from the start or end?
## Sol: trim. trim function is ussed to remove strip whitespace (or other character) from beginning and end of the string. trim function remove the whitespace which is before and after the value.

|