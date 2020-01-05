# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

str = input("Give me a string and I will tell you if it is a palindrome or not.\n")
back = str[::-1]
print(str == back)