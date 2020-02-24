"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

try:
    with open('text_2.txt', 'r', encoding='utf-8') as f:
        content_as_list = f.read().splitlines()
        words_total_count = 0
        for n, line in enumerate(content_as_list, 1):
            words_in_line = len(line.split())
            words_total_count += words_in_line
            print(f'кол-во слов в строке {n}: {words_in_line}')

        print(f'Итого в файле {f.name} {len(content_as_list)}: строк и {words_total_count} слов')
except FileNotFoundError as e:
    print(f'no file: {e}')
except Exception as e:
    print(f'strange error: {e}')
