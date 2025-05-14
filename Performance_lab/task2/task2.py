import argparse
import math

# для запуска скрипта перейдите в директорию task2 и выполните команду ниже
# python task2.py file1.txt file2.txt
parser = argparse.ArgumentParser(description="Приветствие пользователя")
parser.add_argument("path_file_1", help="Путь к файлу 1")
parser.add_argument("path_file_2", help="Путь к файлу 2")

args = parser.parse_args()
path1 = args.path_file_1
path2 = args.path_file_2

with open(path1, 'r') as f:
    lines = [line.strip() for line in f if line.strip()]
    x1, y1 = lines[0].split(' ')
    x1, y1 = int(x1), int(y1)
    r = int(lines[1])

with open(path2, 'r') as f:
    points = [line.strip() for line in f if line.strip()]
    for point in points:
        x2, y2 = point.split(' ')
        x2, y2 = int(x2), int(y2)
        hypotenuse = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if hypotenuse < r:
            print(1)
        elif hypotenuse == r:
            print(0)
        else:
            print(2)
