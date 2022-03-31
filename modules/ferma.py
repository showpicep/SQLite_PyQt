import math
from random import randrange
import random
from modules.pows import fast_pow, powm


def is_prime(num, test_count):
    """Проверка числа на простоту тестом Ферма"""
    for i in range(test_count):
        rnd = random.randint(1, test_count)
        if math.gcd(num, rnd) == 1:
            if powm(rnd, num - 1, num) != 1:
                return False
        else:
            return False

    return True


def nBitRandom(n):

    """ Фунция для генерации n - битного числа """
    return randrange(fast_pow(2, n-1)+1, fast_pow(2, n)-1)
