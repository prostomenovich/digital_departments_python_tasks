# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

indent = 4
ensure_ascii = True


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as csv_file:
        reader = list(csv.DictReader(csv_file))

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(reader, json_file, indent=indent, ensure_ascii=ensure_ascii)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
