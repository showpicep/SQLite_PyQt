def fast_pow(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    p = fast_pow(x, y // 2)
    p *= p
    if y % 2:
        p *= x
    return p

def powm(a: int, b: int, n: int) -> int:
    """
    Функция быстрого возведения числа в степень
     a ^ b Mod n
    """
    a_list = [a]
    b = bin(b).replace('0b', '')
    a_0 = a
    for i in range(1, len(b)):
        if int(b[i]) == 0:
            a_list.append(a_list[i - 1] ** 2 % n)
        else:
            a_list.append(a_0 * a_list[i - 1] ** 2 % n)

    return a_list[-1]

def tryParseInt(s, base=10):
    try:
        return int(s, base),True
    except ValueError:
        return 0,False