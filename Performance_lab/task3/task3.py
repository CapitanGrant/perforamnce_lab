import argparse
import json

# для запуска скрипта перейдите в директорию task3 и выполните команду ниже
# python task3/task3.py task3/values.json task3/tests.json task3/report.json
parser = argparse.ArgumentParser(description="Приветствие пользователя")
parser.add_argument("path_file_1", help="Путь к файлу 1")
parser.add_argument("path_file_2", help="Путь к файлу 2")
parser.add_argument("path_file_3", help="Путь к файлу 3")

args = parser.parse_args()
path_values = args.path_file_1
path_tests = args.path_file_2
path_report = args.path_file_3

print("Начало выполнения программы")


def load_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: Файл {path} не найден")
        exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: Файл {path} имеет неверный формат JSON")
        exit(1)


def save_json(path, data):
    try:
        with open(path, 'w') as file:
            json.dump(data, file)
    except IOError:
        raise f"Ошибка: Не удалось записать файл: {path}"


tests_file = load_json(path_tests)
values_file = load_json(path_values)

print('Обновляю поля value:')


def check_value(test_item, values_map):
    if 'id' in test_item:
        test_id = test_item['id']
        if test_id in values_map:
            test_item['value'] = values_map[test_id]

            print(f"--------> {test_id}: {values_map[test_id]}"" <--------")
    if 'values' in test_item:
        for value in test_item['values']:
            check_value(value, values_map)


values_map = {item['id']: item['value'] for item in values_file['values']}

for test in tests_file['tests']:
    check_value(test, values_map)

save_json(path_report, tests_file)

print(f"Файл успешно сохранен в {args.path_file_3}")
