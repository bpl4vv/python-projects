# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# 1. If the number is a multiple of 4, print out a different message.

# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num1 = int(input("Give me a number and I will tell you if it is even or odd.\n"))
if(num1 % 4 == 0):
    print(num1, "is even and is divisible by 4.")
elif(num1 % 2 == 0):
    print(num1, "is even.")
else:
    print(num1, "is odd.")

num = int(input("Give me another two numbers and I will tell you if the second is a factor of the first.\n"))
check = int(input())

if(num % check == 0):
    print(check, "is a factor of " + str(num) + ".")
else:
    print(check, "is not a factor of " + str(num) + ".")