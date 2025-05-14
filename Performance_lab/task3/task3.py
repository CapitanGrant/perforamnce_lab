import argparse
import json

# для запуска скрипта перейдите в директорию task3 и выполните команду ниже
# python task3.py values.json tests.json report.json
parser = argparse.ArgumentParser(description="Приветствие пользователя")
parser.add_argument("path_file_1", help="Путь к файлу 1")
parser.add_argument("path_file_2", help="Путь к файлу 2")
parser.add_argument("path_file_3", help="Путь к файлу 3")

args = parser.parse_args()
path1 = args.path_file_1
path2 = args.path_file_2
path3 = args.path_file_3

#with open(path1, 'r') as f:
    # json_data = json.load(f)
    # for i in json_data['values']:
    #     print(f'key: {i}')
    #     for k, v in i.items():
    #         print(f'{k}: {v}')

with open(path2, 'r') as file:
    json_data = json.load(file)
    for i in json_data['tests']:
        #print(f'key: {i}')
        for k, v in i.items():
            print(f'{k}: {v}')
# with open(path3, 'r') as f:
#     lines = [line.strip() for line in f if line.strip()]
#     x1, y1 = lines[0].split(' ')
#     x1, y1 = int(x1), int(y1)
#     r = int(lines[1])
