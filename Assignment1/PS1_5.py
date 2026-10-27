import random
from pathlib import Path
import matplotlib.pyplot as plt


def Expression_table():
    digits = '123456789'
    dp = [{0: ['']}] + [{} for _ in range(9)]
    for end in range(1, 10):
        for start in range(end):
            part = digits[start:end]
            number = int(part)
            for value, expressions in dp[start].items():
                for expression in expressions:
                    if start == 0:
                        dp[end].setdefault(number, []).append(part)
                    else:
                        dp[end].setdefault(value + number, []).append(expression + '+' + part)
                        dp[end].setdefault(value - number, []).append(expression + '-' + part)
    return dp[9]


expressions = Expression_table()
Total_solutions = [len(expressions.get(i, [])) for i in range(1, 101)]


def Find_expression(x):
    solutions = expressions.get(x, [])
    for expression in solutions:
        print(f'{expression} = {x}')
    return solutions


def Plot_solutions():
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots(figsize=(8, 3.2))
    ax.plot(range(1, 101), Total_solutions, color='#2864a5', linewidth=1)
    ax.set(xlabel='目标整数', ylabel='表达式数量', xlim=(1, 100), ylim=(0, max(Total_solutions) + 2))
    ax.spines[['top', 'right']].set_visible(False)
    fig.tight_layout()
    Path('assets').mkdir(exist_ok=True)
    fig.savefig('assets/total_solutions.png', dpi=180)
    return fig


if __name__ == '__main__':
    x = random.Random(20261013).randint(1, 100)
    print(f'随机目标：{x}')
    Find_expression(x)
    print('Total_solutions =', Total_solutions)
    for label, value in [('最大', max(Total_solutions)), ('最小', min(Total_solutions))]:
        targets = [i for i, count in enumerate(Total_solutions, 1) if count == value]
        print(f'{label}值：{value}，对应整数：{targets}')
    Plot_solutions()
