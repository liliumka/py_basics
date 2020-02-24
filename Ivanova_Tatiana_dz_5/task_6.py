"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
    Информатика:   100(л)   50(пр)   20(лаб).
    Физика:   30(л)   —   10(лаб)
    Физкультура:   —   30(пр)   —
Пример словаря:
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def get_occupation_hours(data):
    total_sum = 0
    # считаем сумму, выбирая цифры из кажого элемента
    for el in data:
        temp_val = ''.join(filter(lambda n: n.isdigit(), el))
        # пустые элементы заменяем нулем
        total_sum += int(temp_val) if temp_val else 0
    return total_sum


if __name__ == '__main__':
    try:
        with open('text_6.txt', 'r', encoding='utf-8') as f:
            content_as_list = f.read().splitlines()
            print(content_as_list)
            result_dict = {}
            for line in content_as_list:
                key, val_data = line.split(': ')
                val = get_occupation_hours(val_data.split())
                result_dict.setdefault(key, val)
        print(result_dict)
    except FileNotFoundError as e:
        print(f'no file: {e}')
    except Exception as e:
        print(f'strange error: {e}')
