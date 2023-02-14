from math import sqrt

def is_square_num(num):
    if not isinstance(num, int):
        raise TypeError('input object must be instance of int')

    if (round(sqrt(num)) * round(sqrt(num))) == num:
        return True
    else:
        return False


