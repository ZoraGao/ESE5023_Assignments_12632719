def Pascal_triangle(k):
    row = [1]
    for _ in range(1, k):
        row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]
    print(*row)
    return row


if __name__ == '__main__':
    for k in (100, 200):
        print(f'第 {k} 行：')
        Pascal_triangle(k)
