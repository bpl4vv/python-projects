<<<<<<< HEAD
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print("Enter a number and I will output the divisors.")
num = int(input())
list = range(1, num+1)
output = []
for element in list:
    if num % element == 0:
        output.append(element)
print(output)
=======
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print("Enter a number and I will output the divisors.")
num = int(input())
list = range(1, num+1)
output = []
for element in list:
    if num % element == 0:
        output.append(element)
print(output)
>>>>>>> 50f0fd09e2fc0bf4c895e062dc0d5235955a15ad
