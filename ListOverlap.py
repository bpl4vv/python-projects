<<<<<<< HEAD
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:
# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random as r


def overlap(list1, list2):
    return [e for e in set(list1) if e in set(list2)]
    # duplicate = []
    # for ele in list1:
    #     if ele not in duplicate and ele in list2:
    #         result.append(ele)
    #     elif ele not in duplicate:
    #         duplicate.append(ele)
    # return result


# print("Give me 5 numbers.")
# list = []
# for i in range(5):
#     list.append(int(input()))
# print("Give me another 5 numbers.")
# listx = []
# for i in range(5):
#     listx.append(int(input()))

list = []
listx = []

for i in range(5):
    list.append(int(r.random() * i))
    listx.append(int(r.random() * i))

print(list)
print(listx)
print(set(list))
print(set(listx))
print(overlap(list, listx))
=======
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:
# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

def overlap(list1, list2):
    result = []
    result.append(e for e in list1 if e in list2)
    # duplicate = []
    # for ele in list1:
    #     if ele not in duplicate and ele in list2:
    #         result.append(ele)
    #     elif ele not in duplicate:
    #         duplicate.append(ele)
    # return result

print("Give me 5 numbers.")
list = []
for i in range(5):
    list.append(int(input()))
print("Give me another 5 numbers.")
listx = []
for i in range(5):
    listx.append(int(input()))

print(overlap(list,listx))
>>>>>>> 50f0fd09e2fc0bf4c895e062dc0d5235955a15ad
