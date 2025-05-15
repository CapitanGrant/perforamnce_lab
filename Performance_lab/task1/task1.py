from itertools import cycle
import argparse

# для запуска скрипта выполните команду ниже
# python task1/task1.py <ваше значение n> <ваше значение m>
# например:
# python task1/task1.py 4 3
parser = argparse.ArgumentParser(description="Приветствие пользователя")
parser.add_argument("n", type=int, help="Длина кругового массива")
parser.add_argument("m", type=int, help="Длина интервала")

args = parser.parse_args()
n = args.n
m = args.m

print("Начало выполнения программы")

res = []
arr = cycle(range(1, n + 1))
current = next(arr)
while True:
    res.append(str(current))
    for _ in range(m - 1):
        current = next(arr)
    if current == 1:
        break
print('_' * 42)
print('Результат:', ''.join(res))
