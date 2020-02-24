"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк).
- Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
- Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
    Иванов 23543.12
    Петров 13749.32
"""

try:
    with open('text_3.txt', 'r', encoding='utf-8') as f:
        staff_less_20 = []
        staff_salaries = []
        content_as_list = f.read().splitlines()
        print(content_as_list)
        for line in content_as_list:
            person, salary = line.split()
            salary = float(salary)
            staff_salaries.append(salary)
            if salary < 20000:
                staff_less_20.append(person)

    print('Сотрудники с окладом менее 20 тыс.:')
    print(*staff_less_20, sep='\n')
    print(f'Средняя величина дохода сотрудников: {(sum(staff_salaries) / len(staff_salaries)):.2f}')
except FileNotFoundError as e:
    print(f'no file: {e}')
except Exception as e:
    print(f'strange error: {e}')
