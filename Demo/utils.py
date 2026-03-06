import math

def is_prime(n):
    if n < 2:
        raise ValueError('Invalid Input!')

    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            return False

    return True

if __name__ == '__main__':
    print (is_prime(7))