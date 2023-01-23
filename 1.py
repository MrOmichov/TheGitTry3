def s(func):
    def wrapper(v0, v1, t):
        1 / t
        a = func(v0, v1, t)
        print(a)
        global S
        S = (v1*v1 - v0*v0) / (2 * a)
    return wrapper

@s
def a(v0, v1, t):
    a = (v1 - v0) / t
    return a

try:
    n = int(input())
    n1 = int(input())
    n2 = int(input())
    a(n, n1, n2)
    print(S)
except ValueError:
    print('Проверьте коррекность ввода данных')
except ZeroDivisionError:
    print('На нуль делить нельзя: возможно ускорение или время = 0')
