import random


def Matrix_multip(M1, M2):
    result = [[0 for j in range(len(M2[0]))] for i in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                result[i][j] = result[i][j] + M1[i][k] * M2[k][j]
    return result


rng = random.Random(20261013)
M1 = [[rng.randint(0, 50) for _ in range(10)] for _ in range(5)]
M2 = [[rng.randint(0, 50) for _ in range(5)] for _ in range(10)]

if __name__ == '__main__':
    for name, matrix in [('M1', M1), ('M2', M2), ('M1 * M2', Matrix_multip(M1, M2))]:
        print(name)
        for row in matrix:
            print(row)
