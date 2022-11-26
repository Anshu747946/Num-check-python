# checking for prime
def is_prime(computer):
    import math
    # checking for less than 1
    if computer <= 1:
        return False
    # checking for 2
    elif computer == 2:
        return True
    elif computer > 2 and computer % 2 == 0:
        return False
    else:
        # iterating loop till square root of n
        for i in range(3, int(math.sqrt(computer)) + 1, 2):
            # checking for factor
            if computer % i == 0:
                # return False
                return False
    # returning True
    return True


import random as rd

A = int(input('enter starting num: '))
B = int(input('enter end num: '))
computer = rd.randint(A, B)

if computer % 2 == 0:
    print(computer, 'is even number. ')
else:
    print(computer, 'is odd number.')
if computer > 0:
    print(computer, 'is a positive number.')
else:
    print(computer, 'is a negative number.')

if is_prime(computer):
    print(computer, 'is a prime number.')
else:
    print(computer, 'is a composite number.')