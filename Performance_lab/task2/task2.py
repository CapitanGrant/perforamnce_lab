import argparse
import math

# для запуска скрипта task2.py выполните команду ниже
# python task2\task2.py task2\file1.txt task2\file2.txt
parser = argparse.ArgumentParser(description="Приветствие пользователя")
parser.add_argument("path_file_1", help="Путь к файлу 1")
parser.add_argument("path_file_2", help="Путь к файлу 2")

args = parser.parse_args()
path1 = args.path_file_1
path2 = args.path_file_2

print("Начало выполнения программы")


# функция для чтения файла.txt по пути path
def load_txt_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
            return lines
    except FileNotFoundError:
        print(f"Ошибка: Файл {path} не найден")
        exit(1)
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        exit(1)


circle_coordinates = load_txt_file(path1)
x1, y1 = circle_coordinates[0].split(' ')
x1, y1 = int(x1), int(y1)
print("Считываем координаты круга:")
print(f"x1: {x1}, y1: {y1}")
r = int(circle_coordinates[1])
print(f"radius: {r}")

print('_' * 42)
print("Считываем координаты точек:")
points_coordinates = load_txt_file(path2)
for point in points_coordinates:
    x2, y2 = point.split(' ')
    x2, y2 = int(x2), int(y2)
    # вычисляем расстояние от центра окружности
    hypotenuse = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if hypotenuse < r:
        print(f"x2: {x2}, y2: {y2} | результат:", 1)
        print('_' * 42)
    elif hypotenuse == r:
        print(f"x2: {x2}, y2: {y2} | результат:", 0)
        print('_' * 42)
    else:
        print(f"x2: {x2}, y2: {y2} | результат:", 2)
        print('_' * 42)
