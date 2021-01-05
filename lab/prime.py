"""
 Prime Factorization - Have the user enter a number and find all Prime
 Factors (if there are any) and display them.
"""


def is_prime(n):
    """finds if the n is a prime number"""
    if n == 1:
        prime = False
    elif n == 2 or n == 3:
        prime = True
    elif n % 3 == 0 or n % 2 == 0 or n % 5 == 0 or n % 7 == 0:
        prime = False
    else:
        prime = True
    return prime


max_count = int(input("Prime Numbers up to: "))

for i in range(max_count):
    if is_prime(i) is True:
        print(i, " is prime")
    else:
        continue
