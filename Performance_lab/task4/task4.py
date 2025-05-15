import argparse

# для запуска скрипта перейдите в директорию task4 и выполните команду ниже
# python task4\task4.py task4\data.txt
parser = argparse.ArgumentParser(description="Приветствие пользователя")
parser.add_argument("path_file", help="Путь к файлу")

args = parser.parse_args()
path = args.path_file

print("Начало выполнения программы")
try:
    with open(path, 'r') as file:
        nums = [int(line.strip()) for line in file if line.strip()]
except FileNotFoundError:
    print(f"Ошибка: Файл {path} не найден")
    exit(1)

nums.sort()
median = nums[len(nums) // 2]
count = sum(abs(num - median) for num in nums)
print('_' * 42)
print('Резултат:', count)
