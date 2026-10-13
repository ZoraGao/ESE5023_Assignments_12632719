import random


def Least_moves(x):
    moves = 0
    while x > 1:
        if x % 2 == 0:
            x //= 2
        else:
            x -= 1
        moves += 1
    print(moves)
    return moves


if __name__ == '__main__':
    rng = random.Random(20261013)
    for x in [1, 2, 5] + [rng.randint(1, 100) for _ in range(5)]:
        print(f'x = {x}: ', end='')
        Least_moves(x)
