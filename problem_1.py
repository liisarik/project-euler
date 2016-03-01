# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

x = 1000

def sum_of_multiples (limit):
    a = 0
    sum = 0
    while a < limit:
        if (a % 3 == 0) | (a % 5 == 0):
            sum += a
        a += 1
    print(sum)


sum_of_multiples(x)

def sum_of_multiples1 (limit):
    sum = 0
    for a in range(limit):
        if (a % 3 == 0) | (a % 5 == 0):
            sum += a
    print(sum)

sum_of_multiples1(1000)



