# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# 1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

print("Enter your name and age.")
name = str(input())
age = int(input())
output = name + " will turn 100 in the year " + str(100 - age + 2019) + ".\n"
print(output)

# Extra 1
print("How many times do you want to see the message?\n")
times = int(input())
print(times * output)

