import random


def Print_values(a, b, c):
    if a > b:
        if b > c:
            values = (a, b, c)
        elif a > c:
            values = (a, c, b)
        else:
            values = (c, a, b)
    elif b > c:
        # 原图缺失此分支，按降序补全。
        values = (b, a, c) if a > c else (b, c, a)
    else:
        values = (c, b, a)
    print(*values)
    return values


if __name__ == '__main__':
    rng = random.Random(20261013)
    for _ in range(5):
        values = [rng.randint(0, 50) for _ in range(3)]
        print(tuple(values), end=' -> ')
        Print_values(*values)
