def gcd(a: int, b: int) -> int: # Greatest common divisor
    while b:
        a, b = b, a % b
    return a

def phi(n: int) -> int:
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

def double(dot: list[int], a: int, p: int) -> None:
    if dot[1] == 0: return [-1, -1]
    if dot == [-1, -1]: return [-1, -1]

    numerator = (3 * dot[0] ** 2 + a) % p
    denominator = 2 * dot[1]
    
    if numerator % denominator == 0:
        lmbd = numerator / denominator
    else:
        lmbd = (numerator * denominator ** (phi(p) - 1)) % p

    x = int((lmbd ** 2 - 2 * dot[0]) % p)
    y = int((lmbd * (dot[0] - x) - dot[1]) % p)
    return [x, y]


def summ(dot1: list[int], dot2: list[int], p: int) -> list[int]:
    if dot2[0] == dot1[0]: return [-1, -1]
    if dot1 == [-1, -1]: return dot2
    if dot2 == [-1, -1]: return dot1
    
    numerator = (dot2[1] - dot1[1]) % p
    denominator = (dot2[0] - dot1[0]) % p

    if numerator % denominator == 0:
        lmbd = numerator / denominator
    else:
        lmbd = (numerator * denominator ** (phi(p) - 1)) % p

    x = int((lmbd ** 2 - dot1[0] - dot2[0]) % p)
    y = int((lmbd * (dot1[0] - x) - dot1[1]) % p)
    return [x, y]



a = 4 # значение а твоего варианта
p = 11 # Всегда 11
# print(double(([5, 7]), a, p)) # Удвоение точки (3, 5)
# print(double(double(([0, 6]), a, p), a, p)) # Учетверение точки (3, 5)
print(summ([0, 5], [5, 7], p)) # Сложение точки (3, 4) с точкой (5, 6)
