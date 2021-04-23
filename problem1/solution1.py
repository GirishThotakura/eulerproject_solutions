# Problem statement

"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

# Solution 1 using while loop

limit = 1000  # we have to calculate below 1000
num, total = 1, 0  # we are starting from number 1 and considering initial total as 0
while num < limit:
    if num % 3 == 0 or num % 5 == 0:
        total += num
    num = num + 1  # iterator content
print('Simple While Loop Output - ', total)

# Solution 2 using for loop

total = 0
for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        total += num
print('Simple For Loop Output - ', total)


# Solution 3 using list comprehension

print('List Comprehension output - ', sum([num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0]))


# Solution 4 using a user defined function, and check for condition

def divisible(num) -> bool:
    return num % 3 == 0 or num % 5 == 0


limit = 1000  # we have to calculate below 1000
num, total = 1, 0  # we are starting from number 1 and considering initial total as 0
while num < limit:
    if divisible(num):
        total += num
    num = num + 1  # iterator content
print('Function While Loop Output - ', total)


total = 0
for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        total += num
print('Function For Loop Output - ', total)


