########################################
# Author: qw.shen
# Time: 2019.1.3
# Email: shenqingwen_m@163.com
# Intro: Square root.
########################################


def my_sqrt(x, length=4):
    if x <= 0 or not isinstance(length, int) or length < 0:
        return 'error'
    if x == 1 or x == 1.0:
        return round(1, length)
    else:
        if isinstance(x, float):
            x = float(x)
        return _sqrt(x, length)


def _sqrt(x, length):
    up = x if x > 1 else 1.0
    middle = up / 2
    precision = pow(0.1, length)
    middle_pow = pow(middle, 2)
    distance = abs(middle_pow - x)
    while distance > precision:
        down = 0.0
        if middle_pow > x:
            up = middle
        else:
            down = middle
        middle = (up + down) / 2
        middle_pow = pow(middle, 2)
        distance = abs((middle_pow - x))
    return round(middle, length)


def test_sqrt():
    print(my_sqrt(-1, 3))
    print(my_sqrt(2, -2))
    print(my_sqrt(2, 0))
    print(my_sqrt(2, 9))
    print(my_sqrt(0, 3))
    print(my_sqrt(1, 2))
    print(my_sqrt(0.5, 3))
    print(my_sqrt(0.9, 3))
    print(my_sqrt(3, 5))
    print(my_sqrt(3))
    print(my_sqrt(4, 3))
    print(my_sqrt(10, 3))
    print(my_sqrt(100, 5))
    print(my_sqrt(123414, 4))


test_sqrt()
